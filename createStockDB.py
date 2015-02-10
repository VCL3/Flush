import MySQLdb as mdb
import csv
import os

def main():
	# Connect to MySQL, using database stockDB@localhost
	db = mdb.connect(host='localhost', user='weiteliu', db='stockDB')

	#Create cursor to execute SQL commands
	cur = db.cursor() 

	#Create table Stocks in stockDB to store all stock information
	# cur.execute("CREATE TABLE Stocks(Symbol CHAR(10) PRIMARY KEY, Name CHAR(100), MarketCap CHAR(10), Sector CHAR(100))")

	# Load data from NYSE
	with open('Input/NYSE.CSV', 'rU') as csvfile:
		nyse = csv.reader(csvfile)
		nyse.next()
		for row in nyse1:
			cur.execute("INSERT INTO Stocks(Symbol, Name, MarketCap, Sector) VALUES(%s, %s, %s, %s)", row)
		print "NYSE LOADED SUCCESSFULLY"

	# Load data from NASDAQ
	with open('Input/NASDAQ.CSV', 'rU') as csvfile:
		nasdaq = csv.reader(csvfile)
		nasdaq.next()
		for row in nasdaq:
			cur.execute("INSERT INTO Stocks(Symbol, Name, MarketCap, Sector) VALUES(%s, %s, %s, %s)", row)
		print "NASDAQ LOADED SUCCESSFULLY"

	# Commit changes and close connection
	db.commit()		
	cur.close()

if __name__ == "__main__":
	main()