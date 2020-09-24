#!/pi/bin/env python

import time
import serial
import io
ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser),newline="\r")
counter = 0

while 1:
    x = ser.readline()
    print x
