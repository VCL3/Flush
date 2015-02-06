import MySQLdb as mdb
from yahoo_finance import Share
from pprint import pprint

def main():
	data = dict()
	data['TWTR'] = []
	getStockData(data)
	all = data.items()
	print all[0][0], all[0][1][0]




def getStockData(data):
	stock = Share("TWTR")
	# stock.refresh()
	# price = stock.get_price()
	history = stock.get_historical('2015-02-01', '2015-02-04')
	data['TWTR'].append(stock.get_price())


if __name__ == "__main__":
	main()