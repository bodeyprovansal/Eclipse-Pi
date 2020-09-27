
from datetime import datetime

class SingleTestMeasurement:
	def __init__(TM, command, port, devName, host, TCPport):
		TM.creationTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		TM.command = command
		TM.response = "*No Response*\n"
		TM.port = port
		TM.devName = devName
		TM.host = host
		TM.TCPport = TCPport
	
	def getCommand(measurement):
		return measurement.command
	def setCommand(measurement, command):
		measurement.command = command
	def getResponse(measurement):
		return measurement.response
	def setResponse(measurement, response):
		measurement.response = response
		
	#def exportMeasurement(measurement):
	#	send command, response, time to filename 
		
