#!/usr/bin/env python

import pickle
import joblib
from flask import Flask, request, app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
import json

app=Flask(__name__)
bg_classifer_model=joblib.load('bg_model.joblib')

@app.route('/')
def home():
    return render_template('home.html')

#def extract_values(json_obj, values_array):
    #if isinstance(json_obj, dict):
        #for key, value in json_obj.items():
            #extract_values(value, values_array)
    #elif isinstance(json_obj, list):
        #for item in json_obj:
            #extract_values(item, values_array)
    #else:
        #values_array.append(json_obj)
    #return values_array

#@app.route('/predict_api',methods=['POST'])
#def predict_api():
    #data=request.json['data']
    
    
    #new_data=extract_values(data,[])
    
    #n_d=[new_data]
    #print(n_d)
    
    #output=bg_classifer_model.predict(n_d)
    #print(output[0].tolist())
    ##op=jsonify({'prediction': output.tolist()})
    #return render_template("home.html",prediction_text="The prediction for vehicle Insurance is{}".format(output[0].tolist()))
    ##Response 32 bytes [200 OK]&gt;
    ##print(output)
    ##print(output[0])
    ##return jsonify(output[0])
    ##return output
    ##return new_data_arr
@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_output=np.array(data).reshape(1,-1)
    output=bg_classifer_model.predict(final_output)[0]
    return render_template("home.html",prediction_text="The prediction for vehicle Insurance is {}".format(output.tolist()))


if __name__=="__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=4000)
    


