# coding: UTF-8
from urllib.request import urlopen

question = input("请输入关键字：")
type = input("请输入文件类型：")

if type == "图片"：
	fileType = "isch"
else type == "视频":
	fileType = "vid"
	
Url = "https://www.google.com.hk/search?q="+question+"tbm="+fileType
	
html = urlopen(Url)
bsObj = BeautifulSoup(html)
print(bsObj)


