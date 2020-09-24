import serial

print('Opening Pip w method 1:')
ser = serial.Serial('/dev/ttyUSB0')
print("ser.name" + ser.name)
print("ser.is_open")
ser.is_open
ser.write(b'hello\n')
print("ser.close...")
ser.close()
print("ser.is_open?")
ser.is_open

print('Opening Pip w method 2:')
with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
    x = ser.read()
    s = ser.read(10)
    line = ser.readline()
    print(x)
    print(s)
    print(line)
print('Opening Pip w method 3:')
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0,
                    parity=serial.PARITY_EVEN, rtscts=1)
s = ser.read(100)
print(s)


