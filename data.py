import urllib2
# import lxml
# from lxml import html
# from lxml import etree
# import codecs
# import re
# import json
# from pandas.io.data import DataReader
from yahoo_finance import Share
from pprint import pprint



def getStockData(data):
	stock = Share("TWTR")
	# stock.refresh()
	# price = stock.get_price()
	history = stock.get_historical('2015-02-01', '2015-02-04')
	data['TWTR'].append(stock.get_price())
	

def main():
	data = dict()
	data['TWTR'] = []
	getStockData(data)
	all = data.items()
	print all[0][0], all[0][1][0]


if __name__ == "__main__":
	main()