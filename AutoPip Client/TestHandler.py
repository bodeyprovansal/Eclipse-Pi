import pandas
from datetime import datetime
from TestScript import TestScript
class TestHandler():
	def __init__(TH):
		TH.testTime = datetime.now()
		TH.testScripts = []
		TH.testMeasurements = []
		TH.resultsDF = pandas.DataFrame()
		TH.testName = TH.testTime.strftime("%m%d%Y%H%M%S") + ".csv"
		
	def addScript(handler, script):
		newScript = TestScript(script)
		handler.testScripts.append(newScript)
		
	def runScripts(handler):
		for script in handler.testScripts:
			script.runCommands()
			handler.testMeasurements.append(script.exportMeasurements())
		for meas in handler.testMeasurements:
			handler.resultsDF.append(meas, ignore_index=True)
		csv_all = handler.resultsDF.to_csv(handler.testName, quoting = None, header = True)
