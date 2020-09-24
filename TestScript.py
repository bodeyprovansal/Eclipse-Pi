import json
from TestMeasurement import SingleTestMeasurement
from EclipseInterface import EclipseInterface
class TestScript:
	def __init__(TS, scriptFile):
		TS.measurements = []
		f = open('script.JSON',)
		data = json.load(f)
		for meas in data['measurements']:
			TS.measurements.append(SingleTestMeasurement(meas['command'], 
				meas['port'], meas['devName']))
		f.close()

	def showCommands(script):
		for meas in script.measurements:
			print(meas.command)
			#print(meas.response)
			print(meas.port)
			print(meas.devName)
			
	def runCommands(script):
		for meas in script.measurements:
			pip = EclipseInterface(meas.port, meas.devName)
			pip.ser.write(bytes(meas.command + '\n'))
			meas.setResponse(pip.readEclipse())
			print meas.getResponse()
			

