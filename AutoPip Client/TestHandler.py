import pandas
from datetime import datetime
from TestScript import TestScript
class TestHandler():
	def __init__(TH):
		TH.testTime = datetime.now()
		TH.testScripts = []
		TH.testMeasurements = []
		TH.resultsDF = pandas.DataFrame()
		
	def addScript(handler, script):
		newScript = TestScript(script)
		handler.testScripts.append(newScript)
		
	def runScripts(handler):
		for script in handler.testScripts:
			script.runCommands()
			handler.testMeasurements.append(script.exportMeasurements())
		for meas in handler.testMeasurements:
			handler.resultsDF.append(meas, ignore_index=True)
		handler.resultsDF.to_csv(TH.testTime, quoting = None, header = True)
		
