#!/usr/bin/env python

import time
import serial
import requests
import json

URL_GET = "http://18.188.218.25/tests/1"
URL_POST = "http://18.188.218.25/tests/"

response_get = requests.get(url=URL_GET)
#loads in JSON and converts to Python object
data_in = json.loads(response_get.content)
#print("GET Response")
#print(response_get.status_code)
#print(response_get.json())
#print(data_in["name"])
#print(data_in["alias"])
#print(data_in["id"])
#takes a Python object and converts to JSON string
test_obj_out = {
    "name":"API Post Test",
    "alias":"API_POST_01"
}

#response_post = requests.post(url=URL_POST, json=test_obj_out)
#data_out = json.loads(response_post.content)
#print("POST Response")
#print(response_post.status_code)
#print(response_post.json())
#print(data_out["id"])
#print(data_out["alias"])
#print(data_out["name"])

def newPostObj(name, alias, command, result):
    post_obj = {
        "name":name,
        "alias":alias, 
        "command":command,
        "result":result
    }
    return post_obj

def openPippin(pipPort, pipTimeout):
    pip = serial.Serial(
        port=pipPort,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=pipTimeout
    )

    return pip

def printResponse(respName, lines):
    print("%s:\n" %(respName))
    for i in range(0, len(lines)):
        print(lines[i]) 
    

def getResponseFromPippin(out):
    print(out)
    return out
    
def writeToPippin(msg, pip):
    pip = pip
    pip.write(msg + '\r')
    time.sleep(0.05)
    cArray = []
    lArray = [] 
    while (pip.in_waiting > 0):
        nextByte = pip.read(1)
        if(nextByte == '\r' or nextByte == '\n'
            or nextByte == '\r\n' or nextByte == '\n\r'):
                if(len(cArray) > 0):
                    tArray = [None] * len(cArray)
                    for k in range(0, len(cArray)):
                        tArray[k] = cArray[k]
                    textLine = ''.join(tArray)
                    del cArray[:]
                    lArray.append(textLine)
        else:
            cArray += nextByte

    return lArray;    
    
    
    
def closePippin(pip):
    pip.close()
command = 'up'
print("Opening port...")
pip = openPippin('/dev/ttyUSB0', 5)
pip.write('\r\n')
time.sleep(1)
result = writeToPippin(command, pip)

time.sleep(1)
result = writeToPippin(command, pip)

time.sleep(1)
result = writeToPippin(command, pip)

time.sleep(1)
result = writeToPippin(command, pip)

testName = raw_input("Enter Test Name: ")
testAlias = raw_input("Enter Test Alias: ")
postObj = newPostObj(testName, testAlias, command, result)
response_post = requests.post(url=URL_POST, json=postObj)
data_out = json.loads(response_post.content)
print("POST Response")
print(response_post.status_code)
print(response_post.json())
print(data_out["id"])
print(data_out["alias"])
print(data_out["name"])
print(data_out["command"])
print(data_out["result"])
#setModeResp = writeToPippin("accel set mode enabled", pip)
#printResponse("Enable Accel Mode", setModeResp)
#while 1:
    #print("Writing to port...")
    #writeToPippin("help accel", pip)
    
    #time.sleep(1)
    #xyzResp = writeToPippin("accel get xyz", pip)
    #time.sleep(1)
    #printResponse("Get XYZ: ", xyzResp)
    #time.sleep(1)
    #motionResp = writeToPippin("accel get motion", pip)
    #time.sleep(1)
    #printResponse("Get Motion: ", motionResp)
    
    #upResp = writeToPippin('up', pip)
    #printResponse("UP\n", upResp)
    #writeToPippin('help oled', pip)
    #writeToPippin('help', pip)
    #time.sleep(3)
    #userToPippin = raw_input("Enter a command: ")
    #pipResp = writeToPippin(userToPippin, pip)
    #printResponse("Pippin Response", pipResp)
    
