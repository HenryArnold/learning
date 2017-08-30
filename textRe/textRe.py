#_*_ coding:utf-8 _*_
import sys,os
import shutil  #了解一下shutil模块的使用

if len(sys.argv)<=3:
    print("usage: python textRe.py fileName oldText newText [--bak]")
oldText,newText = sys.argv[2],sys.argv[3]

fileName = sys.argv[1]

#open file and bak file
f = open(fileName, 'rb')

if ('--bak' in sys.argv):
    bakFile = open(fileName+'.bak' ,'wb')
    bakFile = f
    bakFile.close()

#replace oldText
for line in f.readlines():
    print (line.replace(oldText,newText))
f.close()


