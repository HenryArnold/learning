#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import sys
import os
retry_limit = 3
retry_count = 0
account_file = 'accounts.txt'
lock_file = 'account_lock.txt'

#允许尝试登陆retry_limit次
while (retry_count < retry_limit):
    username = input("Username:")

    lock_check = open(lock_file) #当输入用户名后，打开LOCK文件检查此用户已经LOCK
    for line in lock_check.readlines(): #循环LOCK文件
        if username in line:
            sys.exit("User %s is locked!" %username)
            #如果LOCK了，就直接退出
			
    password = input("Password:")
	
    f = open(account_file) #打开账号文件
     match_flag = False #默认为Flase，如果用户match上，就设置为True

    for line in f.readlines():
         user,passwd = line.strip('\n').split(' ')
        去掉每行多余的\n并把这一行按空格分成两列，分别赋值为uesr,passwd两个变量

        if (username == user and password == passwd):
            print ('Match!', username)
            match_flag = True
           #相等就把循环外的match_flag变量改为True
    
        f.close()
        if (match_flag == False):
        #如果match_flag为flase,代表上面的循环中根本就没有match上用户名和密码，所以需要继续循环
            print ("username or password is wrong!")
            retry_count +=1
            print ("you can try %d times !",retry_limit-retry_count)
            break
    else:
        print("welcome login learing system!")
        sys.exit()


print("your account is locked !")
f = open(lock_file,'w+')
f.write(username)
f.close()

