from flask import Flask, request, jsonify
import pickle
import os
from Constant.constants import MODEL_DIR,MODEL_NAME


PATH = os.path.join(MODEL_DIR,MODEL_NAME)



app = Flask(__name__)

#Load the trained model 
with open(PATH, 'rb') as file:
    model = pickle.load(file)
print("Model Loded succesfully")

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the POST request
    data = request.form

    # Preprocess the input data
    age = int(data['age'])
    sex = int(data['sex'])
    cigsPerDay = int(data['cigsPerDay'])
    totChol = int(data['totChol'])
    sysBP = int(data['sysBP'])
    glucose = int(data['glucose'])

    # Make a prediction using the loaded model
    prediction = model.predict([[age, sex, cigsPerDay, totChol, sysBP, glucose]])

    # Return the prediction as an API response
    response = {
        'prediction': prediction[0]
    }

    return jsonify(response)

@app.route('/')
def hello():
    # Get the input data from the POST request
    str1  = "Hello world"
    return jsonify(str1)

if __name__ == '__main__':
    app.run()