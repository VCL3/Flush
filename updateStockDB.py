import MySQLdb as mdb
from yahoo_finance import Share
#import progressbar
#from pprint import pprint

def main():
	# Connect to MySQL, using database stockDB@localhost
	db = mdb.connect(host='localhost', user='weiteliu', db='stockDB')

	with db:
		# Create cursor to execute SQL commands
		cur = db.cursor() 

		# Get all symbols
		cur.execute(" SELECT Symbol from Stocks WHERE Sector = 'Technology' ")

		# Fetch all symbols, return list of tuples
		symbols = cur.fetchall()

		print "Numbers of stocks:", len(symbols)

		n = 1
		for symbol in symbols:
			try:
				stock = Share(symbol[0])
				# Get History Data
				history = getHistory(stock)
				print n, " : ", symbol[0], " SUCCESS!"
			except:
				history = [{'Close' : '0', 'High' : '0', 'Low' : '0'}, {'Close' : '0', 'High' : '0', 'Low' : '0'}, {'Close' : '0', 'High' : '0', 'Low' : '0'}, {'Close' : '0', 'High' : '0', 'Low' : '0'}, {'Close' : '0', 'High' : '0', 'Low' : '0'}]
				print n, " : ", symbol[0], " FAIL!"

			# Get High
			high = getHistoryHigh(history)
			if len(high) != 5:
				high = ['0', '0', '0', '0','0']
			cur.execute("INSERT INTO High (Symbol, H5, H4, H3, H2, H1) VALUES (%s, %s, %s, %s, %s, %s)", [symbol[0]] + high)

			# Get Low
			low = getHistoryLow(history)
			if len(low) != 5:
				low = ['0', '0', '0', '0','0']
			cur.execute("INSERT INTO Low (Symbol, L5, L4, L3, L2, L1) VALUES (%s, %s, %s, %s, %s, %s)", [symbol[0]] + low)

			n += 1

			# price = getHistoryPrice(history)
			# cur.execute("INSERT INTO Price (Symbol, P26, P25, P24, P23, P22, P21, P20, P19, P18, P17, P16, P15, P14, P13, P12, P11, P10, P9, P8, P7, P6, P5, P4, P3, P2, P1) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [symbol[0]] + price)

    # for i in range(cur.rowcount):
    #  	row = cur.fetchone()

    # Commit and Disconnect MySQL
	db.commit()
	cur.close()
	print "UPDATE COMPLETED"

	# stock = Share('CACH')
	# history = getHistory(stock)
	# print history
	# high = getHistoryHigh(history)
	# print high

def getHistory(stock):
	history = stock.get_historical('2015-02-04', '2015-02-10')
	if len(history) != 5:
		history = [{'Close' : '0', 'High' : '0', 'Low' : '0'}, {'Close' : '0', 'High' : '0', 'Low' : '0'}, {'Close' : '0', 'High' : '0', 'Low' : '0'}, {'Close' : '0', 'High' : '0', 'Low' : '0'}, {'Close' : '0', 'High' : '0', 'Low' : '0'}]
	return history

# Close price
def getHistoryPrice(history):
	price = []
	for hist in history:
		price.append(hist['Close'])
	return price

def getHistoryHigh(history):
	high = []
	for hist in history:
		high.append(hist['High'])
	return high

def getHistoryLow(history):
	low = []
	for hist in history:
		low.append(hist['Low'])
	return low

def getDayPrice(stock):
	return stock.get_price()

def getDayHigh(stock):
	return stock.get_days_high()

def getDayLow(stock):
	return stock.get_days_low()
	
if __name__ == "__main__":
	main()