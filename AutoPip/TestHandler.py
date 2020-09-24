from datetime import datetime
from TestScript import TestScript
class TestHandler():
	def __init__(TH):
		TH.testTime = datetime.now()
		TH.testScripts = []
		
	def addScript(handler, script):
		newScript = TestScript(script)
		handler.testScripts.append(newScript)
		
	def runScripts(handler):
		for script in handler.testScripts:
			script.runCommands()
		
