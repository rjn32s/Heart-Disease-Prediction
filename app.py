import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the saved pipeline and model
with open('./saved_models/pipeline_model.pkl', 'rb') as file:
    pipeline = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the JSON data from the POST request
    input_data = request.get_json()

    # Convert string values to appropriate data types
    input_data = {k: float(v) if not isinstance(v, float) else v for k, v in input_data.items()}

    # Create a DataFrame from the input_data dictionary
    df = pd.DataFrame.from_dict([input_data])

    # Perform inference using the loaded pipeline
    predictions = pipeline.predict(df.values)

    # Return the predictions as a JSON response
    response = {'predictions': predictions.tolist()}  # Convert predictions to a list
    print(response, type(response))
    return jsonify(response)

if __name__ == '__main__':
    app.run()
