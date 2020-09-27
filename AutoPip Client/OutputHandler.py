import csv
# try install pandas, automatic csv handler
import pandas
#writing to a file using csv
with open('test.csv', mode='w') as output_file:
	output_writer = csv.writer(output_file, delimiter=',', 
			quotechar='"', quoting=csv.QUOTE_MINIMAL)
	output_writer.writerow(['Command', 'Response', 'Device'])
	output_writer.writerow(['command 1', 'response1', 'device1'])
	output_writer.writerow(['command 2', 'response2', 'device2'])
#modifing a file using panda
df = pandas.read_csv('test.csv',
			index_col='Device',
			parseString ='command 1',
			names=['Command', 'Response', 'DeviceName'])
df.to_csv('test_all_command1.csv')

#class Panda:
#	def __init__(PD, fileName):
		


