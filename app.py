from flask import Flask, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
with open("./model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/classify", methods=["POST"])
def classify():
    # Read the data from the request
    data = request.get_json()
    pixels = np.array(data["pixels"]).reshape(1, -1)
    
    # Use the model to make a prediction
    pred = model.predict(pixels)[0]
    
    # Return the result as a JSON response
    return {"class": int(pred)}

if __name__ == "__main__":
    app.run()
