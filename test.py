import csv
import MySQLdb
import os

mydb = MySQLdb.connect(host='localhost', user='weiteliu', db='stockDB')

cursor = mydb.cursor()

csvfile = open('Input/NYSE1.csv', 'rU')
csv_data = csv.reader(csvfile)

for row in csv_data:
	print row
	cursor.execute('INSERT INTO `heating` VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s,    %s, %s, %s, %s, %s, %s, %s ,%s)', row)








