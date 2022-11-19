from flask import Flask, request, Response, send_from_directory
import requests
import json
from flask_cors import CORS
import ibm_db

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "6Um4mZdaiEEL5HIQcUtfZPUwMjauxm0vA_sigkM1ZMrF"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
#payload_scoring = {"input_data": [{"fields": [["Cylinders","Displacement","Horsepower","Weight","Acceleration","ModelYear","Origin"]], "values": [4,7,58,89,1000,568,70]}]}


#API_KEY_NEW = 'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/6ed70a51-2d98-4119-a5bf-eda733928a88/predictions?version=2022-11-17'

app=Flask(__name__)

@app.route('/health-check', methods=['GET'])
def health_check_for_user():
    return Response("Running")


@app.route('/get-key', methods=['GET'])
def get_key():
    API_KEY = "6Um4mZdaiEEL5HIQcUtfZPUwMjauxm0vA_sigkM1ZMrF"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
     API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]
    return Response(mltoken)


@app.route('/get-users', methods=['GET'])
def get_users():
    return get_user()


@app.route('/get-performance', methods=['POST'])
def get_performance_for_user():
    print(request.args)
    query = request.get_json()
    print(query)
    inp = query.get('inp')
    payload_scoring = {"input_data": [{"field": [["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin"]], "values": [
        inp]}]}
    API_KEY = "ghlM0uRRAejCR4xcA7A68hkhTuMQIhYDdI-9S_8ckoVq"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
                                                                                     API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + mltoken}
    url = API_KEY_NEW
    api_response = requests.post(url=url, json=payload_scoring, headers=header)
    return Response(api_response)
  
  if __name__ == '__main__':
    app.run(debug=True)
