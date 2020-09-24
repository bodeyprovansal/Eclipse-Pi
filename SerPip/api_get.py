#!/usr/bin/env python
#make a GET request from helloAPI
#steps first followed from 
#---->https://www.dataquest.io/blog/python-api-tutorial/
import requests
import json
#api.open-notify
#URLA = "http://api.open-notify.org/iss-pass.json"
#parameters = {"lat": 40.71, "lon": -74}

#responseA = requests.get(url=URLA, params=parameters)
#print(responseA.status_code)
#print(responseA.content)
#print(responseA.content)

URL_GET = "http://18.188.218.25/tests/1"
URL_POST = "http://18.188.218.25/tests/"

response_get = requests.get(url=URL_GET)
#loads in JSON and converts to Python object
data_in = json.loads(response_get.content)
print("GET Response")
print(response_get.status_code)
print(response_get.json())
print(data_in["name"])
print(data_in["alias"])
print(data_in["id"])
#takes a Python object and converts to JSON string
test_obj_out = {
    "name":"API Post Test",
    "alias":"API_POST_01"
}

response_post = requests.post(url=URL_POST, json=test_obj_out)
data_out = json.loads(response_post.content)
print("POST Response")
print(response_post.status_code)
print(response_post.json())
print(data_out["id"])
print(data_out["alias"])
print(data_out["name"])


