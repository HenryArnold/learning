import sys
import time
import urllib
import requests
import numpy as np
from bs4 import BeautifulSoup
from openpx1 import Workbook

reload(sys)
sys.setdefaultencoding('utf-8')

#user agents
hds = [{'user-agent':'Mozilla/5.0 (Windows; U; Windows NT; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\{'User-Agent':'Mizilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\{'user-agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

def book_spider(book_tag):
    page_num = 0;
    book_list = []
    try_times = 0

    while(1)
    url = 'http://www.douban.com/tag/'+urllib.quote(book_tag)+'/book?start='+str(page_num*15)
    time.sleep(np.random.rand()*5)

    try:
        reg = urllib.Request(url, headers=hds[page_num%len(hds)])
        source_code = urllib.urlopen(req).read()
        plain_text = str(source_code)
    except(urllib.HTTPError, urllib.URLError),e:
        print(e)
        continue

