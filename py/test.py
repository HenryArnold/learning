"""
this is a zip file pwd crack tool
"""

#coding=UTF-8
import zipfile
import threading

def extractFile(zFile,password):
	try:
		zFile.extractall(pwd=password)
		print("found password:", password)
		return password
	except:
		pass
def main():
	zFile=zipfile.ZipFile('unzip.zip')
	passFile=open('dictionary.txt')
	for line in passFile.readlines():
		password=line.strip('\n')
		t=threading.Thread(target=extractFile,args=（zFile,password))
		t.start()
		
if __name__=='__main__':
	main()
		

