#_*_coding:utf-8 _*_
import sys,os

if (len(sys.argv) <=4):
    print("usage:./fileName.py old_text new_text filename")
    
old_text,new_text = sys.argv[1],sys.argv[2]
file_name = sys.argv[3]

if '--bak'in sys.argv:
    bak_file = '%s.bak' %file_name
else:
    bak_file = None
if bak_file:
