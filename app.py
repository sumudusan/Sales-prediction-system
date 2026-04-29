from flask import Flask, request, render_template
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Global variables
model = None
df_global = None

# Load initial dataset
df = pd.read_csv("Book1.csv")

df["date"] = pd.to_datetime(df["date"])
df["day"] = df["date"].dt.day
df["month"] = df["date"].dt.month
df["day_of_week"] = df["date"].dt.dayofweek

df = pd.get_dummies(df, columns=["product"])

# Ensure both columns exist
for col in ["product_A", "product_B"]:
    if col not in df.columns:
        df[col] = 0

X = df[["price", "day", "month", "day_of_week", "product_A", "product_B"]]
y = df["quantity_sold"]

model = LinearRegression()
model.fit(X, y)

df_global = df.copy()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    price = float(request.form["price"])
    date = pd.to_datetime(request.form["date"])
    product = request.form["product"]

    day = date.day
    month = date.month
    day_of_week = date.dayofweek

    product_A = 1 if product == "A" else 0
    product_B = 1 if product == "B" else 0

    input_data = [[price, day, month, day_of_week, product_A, product_B]]

    prediction = model.predict(input_data)

    return render_template("index.html", prediction=round(prediction[0], 2))


@app.route("/forecast", methods=["POST"])
def forecast():
    price = float(request.form["price"])
    product = request.form["product"]

    product_A = 1 if product == "A" else 0
    product_B = 1 if product == "B" else 0

    today = pd.Timestamp.today()

    dates = []
    sales = []

    for i in range(1, 8):
        future_date = today + pd.Timedelta(days=i)

        input_data = [[
            price,
            future_date.day,
            future_date.month,
            future_date.dayofweek,
            product_A,
            product_B
        ]]

        pred = model.predict(input_data)[0]

        dates.append(str(future_date.date()))
        sales.append(round(pred, 2))

    return render_template("index.html", dates=dates, sales=sales)


@app.route("/upload", methods=["POST"])
def upload():
    global model, df_global

    try:
        file = request.files["file"]
        df = pd.read_csv(file)

        # Process data
        df["date"] = pd.to_datetime(df["date"])
        df["day"] = df["date"].dt.day
        df["month"] = df["date"].dt.month
        df["day_of_week"] = df["date"].dt.dayofweek

        df = pd.get_dummies(df, columns=["product"])

        # Ensure both columns exist
        for col in ["product_A", "product_B"]:
            if col not in df.columns:
                df[col] = 0

        X = df[["price", "day", "month", "day_of_week", "product_A", "product_B"]]
        y = df["quantity_sold"]

        model = LinearRegression()
        model.fit(X, y)

        df_global = df.copy()

        avg_sales = df["quantity_sold"].mean()

        return render_template("index.html",
                               message="File uploaded & model trained!",
                               avg=round(avg_sales, 2))

    except Exception as e:
        return render_template("index.html", message=f"Error: {str(e)}")


@app.route("/insights")
def insights():
    if df_global is None:
        return render_template("index.html", message="No data available")

    total = df_global.groupby("product_A")["quantity_sold"].sum()

    return render_template("index.html", insights=total.to_dict())


if __name__ == "__main__":
    app.run(debug=True)