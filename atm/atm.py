#!/usr/bin/env python
#coding:utf-8

import time
import sys


#initilize time
account = {'xiaoming':{'password':'abcdefg', 'status':0 , 'money':15000 } , 'daming':{'password':'asdf','status':0 , 'money':13000}}
queryInfo = {'xiaoming':{'2017/8/14':{'12:00:00':'take 500$' , '12:03:02':'pay back 600$'} , '2017/8/12':{'12:00:03':'transfer 50$ to daming'}}, 'daming':{'2017/8/14':{'12:00:00':'take 500$' , '12:03:02':'pay back 600$'} , '2017/8/12':{'12:00:03':'transfer 50$ to daming'}}}





#login time
def login():
    print("\t\t\033[36m" + "welcom simple atm system " + "\033[0;39m" )
    print("\t please enter your uername and password")
    global username
    global success
    global nowUser
    global i
    username = input("\t username: ")
    try:
        checkAccount()
    except:
        print("\t check account error")
    password = input("\t password: ")
    try:
        if password == account[username]['password']:
            print("\t\t\033[32m" + "login success !" + "\033[0;39m")
            success = 1
            nowUser = username
            
        else:
            print("\t username or password is error !")
            i += 1
            success = 0

    except:
        print("\t username or password is error !")
        i += 1

def lockAccount():
    global i
    if i >= 3:
        account[username]['status'] = 1
    else:
        return

#show options
def showOption():
        print("\t 1 take money  ")
        print("\t 2 query trade info ")
        print("\t 3 pay back money  ")
        print("\t 4 transfer money")
        print("\t 5 check accout")
        print("\t 6 exit")
        print("\t option ")


#option control time
def option():
 
    def option1(): 

        #withdraw money
        print("\t how much do you want to withdaw   ")
        takeMoney = float(input("\t :"))
        account[nowUser]['money'] -= takeMoney
        print("\t split out money ....")
        time.sleep(5)
        print("\t withdram success\n\n")
        option()

        #add information

    def option2():

        #query information
        print("\t please input query date")
        date = input("\t : ")
        try:
            for i in queryInfo[nowUser][date]:
                print( i  +":"+  queryInfo[nowUser][date][i])
        except:
            print("\t date is error, please input correct date" )
        print("\n\n")
        option()

    def option3():

        #pay back money
        print("\t how much do you want to payback")
        payBack = float(input("\t:"))
        account[nowUser]['money'] -= payBack
        print("\t pay back money success")
        print("\n\n")
        option()

        ##add information

    def option4():
        print("\t which account do you want to transfer money")
        toUser = input("\t: ")
        print("\t how much money do you want to transfer")
        transferMoney = input("\t :")
        try:
            account[toUser]['money'] += transferMoney
            userinfo[nowUser]['money'] -= transferMoney
        except:
            print("\t account is not exist")
        print("\n\n")
        option()

    def option5():
        print("\t\t account information")
        print("\t [1]account username\t"+ nowUser )
        print("\t [2]account password\t"+ account[nowUser]["password"])
        print("\t [3]account money \t" + str(account[nowUser]["money"]))
        print("\t\t")
        option()

    def option6():
        print("\t exit success")
        time.sleep(3)
        sys.exit()

   
    showOption()   
    global choice
    choice = input("\t : ")
    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    elif choice == "3":
        option3()
    elif choice == "4":
        option4()
    elif choice == "5":
        option5()
    else:
        option6()

def checkAccount():
    global username
    if account[username]['status'] :
        print("\t your account is locked ")
        sys.exit()
    else:
        return

if __name__ == '__main__':
    #initlize all variables
    username ='null' 
    nowUser = 'null'
    success = 0
    i = 0

    while True:
        login()
        lockAccount()
        if success:
            break
    option()


