#只爬取单个网站
#提供 1：目标网址 2：目标名
#返回 1：目标url

#1. 遍历域名下所有网站 2. 查找是否匹配
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random

random.seed(datetime.datetime.now())
Url = input("target url:")
target = input("target name:")
links=[target]

def getLocation(Url):
	print("   waite .....")
	try:
		html = urlopen("http://"+Url)
	except HTTPErrot as e:
		print (e)
	bsObj = BeautifulSoup(html,"lxml")
	judge = target in str(bsObj)
	if judge:
		print("[+]"+Url)
		return judge
	else:
		return judge
	
def getLink:
	links = links.append(bsObj.findAll("a",href=re.compile("^(?!#)*")))
	print(links)
	
def traverse:
	
	