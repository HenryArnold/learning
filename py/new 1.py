from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

page = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj, includeUrl):
	internalLinks = []
	for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internalLinks:
				internalLinks.append(link.attrs['href'])
	return internalLinks
	
def getExternalLinks(bsObj, excludelUrl):
	externalLinks = []
	for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludelUrl+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks
	
def splitAddress(address):
	addressParts = address.replace("http://","").split("/")
	return addressParts
	
def getRandomExternalLink(startPage):
	html = urlopen(startPage)
	bsObj = BeautifulSoup(html)
	externalLinks = getExternalLinks(bsObj, splitAddress(startPage)[0])
	if len(externalLinks) == 0:
		internalLinks = getInternalLinks(startPage)
		return getNextExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
	else:
		return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
	externalLink = getRandomExternalLink("http://oreilly.com")
	print("random externalLink :"+externalLink)
	followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")
	
