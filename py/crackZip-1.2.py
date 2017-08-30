"""
fake code: crack zip pwd
"""
"""
python 提供了zip文件的提取压缩模块---zipfile
我们可以用extractall()函数抽取文件，参数为密码，如果密码正确
返回正确，密码错误抛出异常
"""
"""这里我们可以学一下多线程,加快破解速度。--- threading模块"""
""" vsersion-1.2---多线程"""

#coding=UTF-8

import zipfile
import threading

function ExtractFile(zFile,password)
   try
      zFile.extractall(pwd=password)
	  print("found password:",password)
   except
      pass
function mian()
   zFile=zipfile.ZipFile('unzip.zip')
   passFile=open('dictionary.txt')
   for line in passFile.readlines()
      password=line.strip('\n') //删除每一行末尾的换行符
      t=threading.Thread(target=extractFile,args=(zFile,password))
      t.start()
	  
main()

	  