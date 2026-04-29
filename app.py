from flask import render_template
from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)


df = pd.read_csv("Book1.csv")

df["date"] = pd.to_datetime(df["date"])
df["day"] = df["date"].dt.day
df["month"] = df["date"].dt.month
df["day_of_week"] = df["date"].dt.dayofweek

df = pd.get_dummies(df, columns=["product"])

X = df[["price", "day", "month", "day_of_week", "product_A", "product_B"]]
y = df["quantity_sold"]

model = LinearRegression()
model.fit(X, y)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    price = float(request.form["price"])
    date_input = request.form["date"]
    product = request.form["product"]

    date = pd.to_datetime(date_input)

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
    predictions = []

    for i in range(1, 8):
        future_date = today + pd.Timedelta(days=i)

        day = future_date.day
        month = future_date.month
        day_of_week = future_date.dayofweek

        input_data = [[price, day, month, day_of_week, product_A, product_B]]

        pred = model.predict(input_data)[0]

        predictions.append({
            "date": str(future_date.date()),
            "sales": round(pred, 2)
        })

    return render_template("index.html", forecast=predictions)

if __name__ == "__main__":
    app.run(debug=True)