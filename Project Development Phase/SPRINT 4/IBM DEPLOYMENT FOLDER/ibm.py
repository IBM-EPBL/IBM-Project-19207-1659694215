import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "Ejy_L079WlxpMJ1ZEAHGwPqTFCgkyfaCvW5SVixjuK7S"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [['do','ph','co','bod','na','tc','year']], "values": [[6.7,7.5,203.0,6.940049,0.1,27.0,2014]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/52167cac-2e49-4b19-b10b-0da12af7d3ba/predictions?version=2022-11-14', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
y_pred=pred['predictions'][0]['values'][0][0]
print(y_pred)