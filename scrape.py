import urllib2
import string
import lxml
from lxml import html
from lxml import etree
import codecs
import re
import json
from pandas.io.data import DataReader



def main();
	data = DataReader('AAPL','yahoo',start = '1950-1-1', end = '2013-12-1')
	print type(data)

if __name__ == "__main__":
	main()