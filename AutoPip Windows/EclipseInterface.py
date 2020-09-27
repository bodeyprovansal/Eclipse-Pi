import serial, string, time


counter=0
ret = '\r'
nl = '\n'
rn = '\r\n'

##while 1:
 ##   ser.write(b'Write counter: %d \n'%(counter))
 ##   print("Printed: %d\n"%(counter))
  #  time.sleep(1)
  #  counter += 1
  #  readText = ser.readline()
  #  print(readText)
#ser.close()

class EclipseInterface:
    def __init__(EI, port, devName):
        EI.port = port
        EI.devName = devName
        EI.ser = serial.Serial(EI.port, baudrate = 9600, parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
    
    def printInfo(interface, junk):
        print("port: " + interface.port + "\n")
        print("device name: " + interface.devName + "\n")
        print(junk + "\n")
        return 
        
    def writeEclipse(interface, command):
        interface.ser.write(command)
        time.sleep(1)
        return
    
    def readEclipse(interface):
    #while output != "":
        #output = pip.readline()
        #print output
        rx_data = interface.ser.read()
        time.sleep(0.3)
        data_left = interface.ser.inWaiting()
        rx_data += interface.ser.read(data_left)
        rx_data.decode('utf-8')
        return rx_data

    def closeEclipse(interface):
        interface.ser.close()
        return