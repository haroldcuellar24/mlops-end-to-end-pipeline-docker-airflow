from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Cargar
model = joblib.load('models/modelo_random_forest.pkl')

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)[0]
    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)