import MySQLdb as mdb
import csv
import os

def main():
	# Connect to MySQL, using database stockDB@localhost
	db = mdb.connect(host='localhost', user='weiteliu', db='stockDB')

	#Create cursor to execute SQL commands
	cur = db.cursor() 

	'''
	# Initialize all stock information. DO NOT EXECUTE!
	
	# Create table Stocks in stockDB to store all stock information
	cur.execute("CREATE TABLE Stocks(Symbol CHAR(10), Name CHAR(100), MarketCap CHAR(20), Sector CHAR(100), Exchange CHAR(10), PRIMARY KEY(Symbol))")

	# Load data from NYSE
	with open('Input/NYSE.CSV', 'rU') as csvfile:
		nyse = csv.reader(csvfile)
		nyse.next()
		for row in nyse:
			cur.execute("INSERT INTO Stocks(Symbol, Name, MarketCap, Sector, Exchange) VALUES(%s, %s, %s, %s, %s)", row + ['NYSE'])
		print "NYSE LOADED SUCCESSFULLY"

	# Load data from NASDAQ
	with open('Input/NASDAQ.CSV', 'rU') as csvfile:
		nasdaq = csv.reader(csvfile)
		nasdaq.next()
		for row in nasdaq:
			cur.execute("INSERT INTO Stocks(Symbol, Name, MarketCap, Sector, Exchange) VALUES(%s, %s, %s, %s, %s)", row + ['NASDAQ'])
		print "NASDAQ LOADED SUCCESSFULLY"

	# Create table Price
	cur.execute("CREATE TABLE Price(Price_ID SMALLINT NOT NULL AUTO_INCREMENT, Symbol CHAR(10), P1 CHAR(10), P2 CHAR(10), P3 CHAR(10), P4 CHAR(10), P5 CHAR(10), P6 CHAR(10), P7 CHAR(10), P8 CHAR(10), P9 CHAR(10), P10 CHAR(10), P11 CHAR(10), P12 CHAR(10), P13 CHAR(10), P14 CHAR(10), P15 CHAR(10),P16 CHAR(10), P17 CHAR(10), P18 CHAR(10), P19 CHAR(10), P20 CHAR(10), P21 CHAR(10), P22 CHAR(10), P23 CHAR(10), P24 CHAR(10), P25 CHAR(10), P26 CHAR(10), PRIMARY KEY (Price_ID), FOREIGN KEY(Symbol) REFERENCES Stocks(Symbol))")
	
	# Create table High & Low
	cur.execute("CREATE TABLE High(High_ID INT NOT NULL AUTO_INCREMENT, Symbol CHAR(10), H1 CHAR(10), H2 CHAR(10), H3 CHAR(10), H4 CHAR(10), H5 CHAR(10), H6 CHAR(10), H7 CHAR(10), H8 CHAR(10), H9 CHAR(10), PRIMARY KEY (High_ID), FOREIGN KEY (Symbol) REFERENCES Stocks(Symbol))")
	cur.execute("CREATE TABLE Low(Low_ID INT NOT NULL AUTO_INCREMENT, Symbol CHAR(10), L1 CHAR(10), L2 CHAR(10), L3 CHAR(10), L4 CHAR(10), L5 CHAR(10), L6 CHAR(10), L7 CHAR(10), L8 CHAR(10), L9 CHAR(10), PRIMARY KEY (Low_ID), FOREIGN KEY (Symbol) REFERENCES Stocks(Symbol))")

	# END OF CODE
	'''
	
	# Create table MACD

	# Create Table Stochastics K & D

	db.commit()		
	cur.close()

if __name__ == "__main__":
	main()