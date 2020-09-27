import json, time, pandas
from TestMeasurement import SingleTestMeasurement
from EclipseInterface import EclipseInterface
class TestScript:
	def __init__(TS, scriptFile):
		TS.measurements = []
		f = open(scriptFile,)
		data = json.load(f)
		TS.name = data['scriptName']
		for meas in data['measurements']:
			TS.measurements.append(SingleTestMeasurement(meas['command'], 
				meas['port'], meas['devName']))
			
		f.close()
		TS.dataFrame = {'Command Sent': [],
				'Response':[],
				'Port': [],
				'Device Name': []}
		

	def showCommands(script):
		for meas in script.measurements:
			print(meas.command)
			#print(meas.response)
			print(meas.port)
			print(meas.devName)
			
	def runCommands(script):
		measCount = 0
		for meas in script.measurements:
			pip = EclipseInterface(meas.port, meas.devName)
			pip.ser.write(bytes(meas.command + '\r'))
			meas.setResponse(pip.readEclipse())
			print meas.getResponse()
			script.dataFrame['Command Sent'].append(meas.command)
			script.dataFrame['Response'].append(meas.response)
			script.dataFrame['Port'].append(meas.port)
			script.dataFrame['Device Name'].append(meas.devName)
			time.sleep(3)
			measCount += 1
			pip.ser.close()
		
	def exportMeasurements(script):
		pandasDF = pandas.DataFrame(script.dataFrame)
		csv_ts = pandasDF.to_csv(script.name, quoting = None, header = True)
		#print('\nExport Results:\n, csv_ts)
