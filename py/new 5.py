import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseUrl ="http://pythonscraping.com"

def getAbsoluteURL(baseUrl, source):
	if source.startswith("http://www."):
		url  = "http://"+source[11:]
	elif source.startswith("http://"):
		url = source
	