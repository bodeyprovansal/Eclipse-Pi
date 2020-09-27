from TestHandler import TestHandler
from EclipseHTTPServer import EclipseHTTPServer
#Test Handler starts a new Test
newTest = TestHandler()
newServer = EclipseHTTPServer("test", 12345, "192.168.1.188")
#Tests are composed of TestScripts
#TestScripts are composed of TestMeasurements
#TestMeasurements are composed of:
	#datetime the measurement was taken
	#command(s)
	#a port to receive a command
	#a friendly name for the device at that port
	#response(s) from that port
print("---- Start -----")
newTest.addScript('script_two_devices.JSON')
newTest.runScripts()
print("---- End -----")

