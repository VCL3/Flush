import MySQLdb as mdb
import csv
import os

def main():
	# Connect to MySQL, using database stockDB@localhost
	db = mdb.connect(host='localhost', user='weiteliu', db='stockDB')

	#Create cursor to execute SQL commands
	cur = db.cursor() 

	# Create table Price
	cur.execute("CREATE TABLE Price(Symbol CHAR(10) PRIMARY KEY")

	'''
	# Initialize all stock information. DO NOT EXECUTE ANY MORE!!!
	
	# # Create table Stocks in stockDB to store all stock information
	# cur.execute("CREATE TABLE Stocks(Symbol CHAR(10) PRIMARY KEY, Name CHAR(100), MarketCap CHAR(20), Sector CHAR(100), Exchange CHAR(10))")

	# # Load data from NYSE
	# with open('Input/NYSE.CSV', 'rU') as csvfile:
	# 	nyse = csv.reader(csvfile)
	# 	nyse.next()
	# 	for row in nyse:
	# 		cur.execute("INSERT INTO Stocks(Symbol, Name, MarketCap, Sector, Exchange) VALUES(%s, %s, %s, %s, %s)", row + ['NYSE'])
	# 	print "NYSE LOADED SUCCESSFULLY"

	# # Load data from NASDAQ
	# with open('Input/NASDAQ.CSV', 'rU') as csvfile:
	# 	nasdaq = csv.reader(csvfile)
	# 	nasdaq.next()
	# 	for row in nasdaq:
	# 		cur.execute("INSERT INTO Stocks(Symbol, Name, MarketCap, Sector, Exchange) VALUES(%s, %s, %s, %s, %s)", row + ['NASDAQ'])
	# 	print "NASDAQ LOADED SUCCESSFULLY"

	# END OF CODE
	'''

	# Commit changes and close connection
	db.commit()		
	cur.close()

if __name__ == "__main__":
	main()