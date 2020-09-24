from TestHandler import TestHandler

#Test Handler starts a new Test
newTest = TestHandler()
#Tests are composed of TestScripts
#TestScripts are composed of TestMeasurements
#TestMeasurements are composed of:
	#datetime the measurement was taken
	#command(s)
	#a port to receive a command
	#a friendly name for the device at that port
	#response(s) from that port
print("---- Start -----")
newTest.addScript('script.JSON')
newTest.runScripts()
print("---- End -----")

