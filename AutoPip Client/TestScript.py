import json, time, pandas
from TestMeasurement import SingleTestMeasurement
from EclipseInterface import EclipseInterface
from EclipseHTTPClient import EclipseHTTPClient
class TestScript:
    def __init__(TS, scriptFile):
        TS.measurements = []
        f = open(scriptFile,)
        data = json.load(f)
        TS.name = data['scriptName']
        for meas in data['measurements']:
            TS.measurements.append(SingleTestMeasurement(meas['command'], 
                meas['port'], meas['devName'], meas['host'], meas['tcp_port']))
            
        f.close()
        TS.dataFrame = {'Command Sent': [],
                'Response':[],
                'Port': [],
                'Device Name': [],
                'Host':[]}
        

    def showCommands(script):
        for meas in script.measurements:
            print(meas.command)
            #print(meas.response)
            print(meas.port)
            print(meas.devName)
            
    def runCommands(script):
        measCount = 0
        for meas in script.measurements:
            if(meas.host == 'localhost'):
                #script.runLocalCommand(meas)
                pip = EclipseInterface(meas.port, meas.devName)
                pip.writeEclipse(bytes(meas.command, encoding='utf-8'))
                meas.setResponse(pip.readEclipse())
                print (meas.getResponse())
                script.dataFrame['Command Sent'].append(meas.command)
                script.dataFrame['Response'].append(meas.response)
                script.dataFrame['Port'].append(meas.port)
                script.dataFrame['Device Name'].append(meas.devName)
                script.dataFrame['Host'].append(meas.host)
                time.sleep(3)
                measCount += 1
                pip.ser.close()
            else:
                request = EclipseHTTPClient(meas.host, int(meas.TCPport), meas.port, meas.command)
                time.sleep(3)
                response = request.getResponse()
                print("Response: " + response.decode('utf-8'))
                meas.setResponse(response)
                script.dataFrame['Command Sent'].append(meas.command)
                script.dataFrame['Response'].append(meas.response)
                script.dataFrame['Port'].append(meas.port)
                script.dataFrame['Device Name'].append(meas.devName)
                script.dataFrame['Host'].append(meas.host)
                #script.runRemoteCommand(meas)
            

    def runLocalCommand(script, meas):
        pip = EclipseInterface(meas.port, meas.devName)
        pip.ser.write(bytes(meas.command + '\r'), 'utf-8')
        meas.setResponse(pip.readEclipse())
        print (meas.getResponse())
        script.dataFrame['Command Sent'].append(meas.command)
        script.dataFrame['Response'].append(meas.response)
        script.dataFrame['Port'].append(meas.port)
        script.dataFrame['Device Name'].append(meas.devName)
        script.dataFrame['Host'].append(meas.host)
        time.sleep(3)
        measCount += 1
        pip.ser.close()

    def runRemoteCommand(script, meas):
        request = EclipseHTTPClient(meas.host, meas.port, meas.command)
        time.sleep(3)
        response = request.msg_from_server
        print(response.decode('ascii'))

    def exportMeasurements(script):
        pandasDF = pandas.DataFrame(script.dataFrame)
        csv_ts = pandasDF.to_csv(script.name, quoting = None, header = True)
        #print('\nExport Results:\n, csv_ts)
