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



@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    price = data["price"]
    day = data["day"]
    month = data["month"]
    day_of_week = data["day_of_week"]
    product_A = data["product_A"]
    product_B = data["product_B"]

    input_data = [[price, day, month, day_of_week, product_A, product_B]]

    prediction = model.predict(input_data)

    return jsonify({
        "predicted_sales": float(prediction[0])
    })


if __name__ == "__main__":
    app.run(debug=True)