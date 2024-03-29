from TestHandler import TestHandler
from EclipseHTTPClient import EclipseHTTPClient

#newClient = EclipseHTTPClient("192.168.1.172", 9090, "Hello Server")
#from EclipseHTTPServer import EclipseHTTPServer
#Test Handler starts a new Test
newTest = TestHandler()
#newServer = EclipseHTTPServer("test", 12345, "192.168.1.188")
#Tests are composed of TestScripts
#TestScripts are composed of TestMeasurements
#TestMeasurements are composed of:
	#datetime the measurement was taken
	#command(s)
	#a port to receive a command
	#a friendly name for the device at that port
	#response(s) from that port
print("---- Start -----")
newTest.addScript('pip_local_http_01.JSON')
#newTest.addScript('win_to_pi.JSON')
#newTest.addScript('one_device_localhost_windows.JSON')
#newTest.addScript('win_to_pi_accel.JSON')
newTest.runScripts()
print("---- End -----")

