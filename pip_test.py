import json

from EclipseInterface import EclipseInterface 
from TestMeasurement import SingleTestMeasurement
from TestScript import TestScript

#devices = ['/dev/ttyUSB0'']

#pip = EclipseInterface('/dev/ttyUSB0', 'Pippin - Alpha')
newScript = TestScript('script.JSON')


#newScript.showCommands()
newScript.runCommands()
ret = '\r'
nl = '\n'
rn = '\r\n'

#pip.printInfo("also print this")

#c1 = "hello"
#pip.writeEclipse(c1 + ret)
#t1 = SingleTestMeasurement(c1, pip.readEclipse()) 
#command = t1.getCommand()
#response = t1.getResponse()
print("----")
#print("t1 time: " + nl + t1.creationTime)
#print("t1 command: " + nl + command + nl)
#print("t1 response: " + nl + response + nl)
print("----")
#pip.writeEclipse("up" + ret)
