import pickle
from flask import Flask, request, jsonify, render_template, url_for
import numpy as np
import pandas as pd
import os

app = Flask(__name__) #Initialize the flask App

# Use os.path.join for cross-platform compatibility
model_path = os.path.join(os.path.dirname(__file__), 'regmodel.pkl')
scalar_path = os.path.join(os.path.dirname(__file__), 'scaling.pkl')

regmodel = pickle.load(open(model_path, 'rb'))
scalar = pickle.load(open(scalar_path, 'rb'))

@app.route('/') #Define the route for the homepage
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        json_data = request.get_json()
        if 'data' not in json_data:
            return jsonify({'error': 'Missing "data" key in JSON'}), 400

        data = json_data['data']
        print(data)
        print(np.array(list(data.values())).reshape(1, -1))
        new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
        output = regmodel.predict(new_data)
        print(output[0])
        return jsonify(output[0])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)[0]
    return render_template("home.html",prediction_text="The House price prediction is {}".format(output))

if __name__=="__main__":
    app.run(debug=True)