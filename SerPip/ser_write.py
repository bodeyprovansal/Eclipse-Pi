#!/usr/bin/env python

import time
import serial
import threading

CHAR_ARRAY_SIZE = 1000
STRING_ARRAY_SIZE = 256
CMD_TIMEOUT = 2000

continueReading = True
displayReceivedTextFromPippin = True
continueRunning = True

charArray = [0] * CHAR_ARRAY_SIZE
receivedLineArray = [] * STRING_ARRAY_SIZE

charArrayIndex = 0
lineArrayIndex = 0


def openPippin(pipPort, pipTimeout):
    pip = serial.Serial(
        port=pipPort,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=pipTimeout
    )
    continueReading = True
    return pip
def getLinesFromPippin(lines):
    print("getLineFromPippin:\n")
    for i in range(0, len(lines)):
        print(lines[i]) 
    return lines

def getResponseFromPippin(out):
    print(out)
    return out


def readFromPippin(pip):
    global charArrayIndex
    print("readFromPippin starting")
    for i in range(0, CHAR_ARRAY_SIZE):
        charArray[i] = '0'
    while(continueReading):
        writeToPippin('hello from the thread', pip)
        c = pip.read(1)
        if((c != '\n') and (c != '\r')):
            charArray[charArrayIndex] = c
            charArrayIndex += 1
        if((c == '\n') or (c == '\r')):
            if(charArrayIndex > 0):
                charArrayTrunc = ['0'] * charArrayIndex
                for k in range(0, charArrayIndex):
                    charArrayTrunc[k] = charArray[k]
                print(charArrayTrunc)
                #textLine = charArrayTrunc
                if(displayReceivedTextFromPippin):
                    print(textLine)
                for i in range(0, CHAR_ARRAY_SIZE):
                    charArray[i] = '0'
                charArrayIndex = 0
                receivedLineArray[lineArrayIndex % STRING_ARRAY_SIZE] = textLine
                lineArrayIndex += 1
        print("thread is still running...")
        
        time.sleep(1)
    
    closePippin()
                
    

def writeToPippin(msg, pip):
    rv = 1
    pip = pip
    pip.write(msg + '\r')
    time.sleep(0.05)
    #rec = []
    pbuf = []
    out = ''
    counter = 0
    cArray = []
    lArray = [None] * 256
    lIndex = 0
    while (pip.in_waiting > 0):
        nextByte = pip.read(1)
        if(nextByte == '\r' or nextByte == '\n'
            or nextByte == '\r\n' or nextByte == '\n\r'):
                if(len(cArray) > 0):
                    tArray = [None] * len(cArray)
                    for k in range(0, len(cArray)):
                        tArray[k] = cArray[k]
                    textLine = ''.join(tArray)
                    #print(textLine)
                    getResponseFromPippin(textLine)
                    del cArray[:]
                    lArray[lIndex] = textLine
                    lIndex += 1
        else:
            cArray += nextByte
        if pbuf:
            rv = 0           
    return rv
    
    
    
def closePippin(pip):
    pip.close()
pip = openPippin('/dev/ttyUSB0', 5)
while continueRunning:
    
    userToPippin = raw_input("Enter a command: ")
    writeToPippin(userToPippin, pip)
    print("Help, Gandalf!")
    writeToPippin('up', pip)
    time.sleep(1)
    writeToPippin('down', pip)
    time.sleep(1)
    
