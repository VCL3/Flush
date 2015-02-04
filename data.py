import urllib2
# import lxml
# from lxml import html
# from lxml import etree
# import codecs
# import re
# import json
# from pandas.io.data import DataReader

from yahoo_finance import Share
import pprint





def getStockData():
	stock = Share("FB")
	price = stock.get_price()
	print price

def main():
	getStockData()





if __name__ == "__main__":
	main()