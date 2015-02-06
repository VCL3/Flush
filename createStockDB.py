import MySQLdb as mdb
import sys

def main():
	#Create connection
	db = mdb.connect(host='localhost', user='weiteliu', db='stockDB')

	with db:
		#Create cursor
		cur = db.cursor() 

		cur.execute("CREATE TABLE Stocks(Ticker CHAR(10) PRIMARY KEY, Price INT)")

		cur.execute("INSERT INTO Stocks(Ticker) VALUES('TWTR')")









if __name__ == "__main__":
	main()