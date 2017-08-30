#!/usr/bin/env python
# _*_ coding:utf8 _*_

import time

#遍历字典
def dicTra(Dict):
    try:
        Dict.values()[0][0]
    except TypeError:
        #若dict.values()[][]报出TypeError错误，表明Dict字典为商品字典，那么打印商品信息
        print ('''\n\t\t\t\033[33;lm本商城提供如下商品：\n\n\t\t商品名称\t商品单价\033[0m''')
        for i in Dict:
            print('''\t\t\t%s:\t\t%s\n'''%(i,Dict[i]))
    except IndexError:
    #若Dict.values()[][]报出IndexError错误，则Dict字典为空，说明未进行任何购买操作，购物车为空，那么屏幕打印后续信息
        print ('''\n\t\t\t\033[31;1m您未在本商城购买任何物品!! \033[0m''')
    else:
    #若Dict.values()[0][0],不报错，那么证明该Dict为购物车字典，并且购买了商品，那么将购物车表打印
        print('''\n\t\t\t\033[31;1m您购买的商品为:\033[0m\n\n\t\t\t\033[32;1m商品名称\t商品数量\t商品总价\033[0m''')
        for i in Dict:
            print('''\t\t\t%s:\t\t%s\t\t%s\n'''%(i,Dict[i][0],Dict[i][1]))
        print('''\t\t\t您一共消费：\033[31;1m%s\033[0m,您的余额为：\033[31;1m%s\033[0m\n'''%(Total_Salary - Balance,Balance))
#判断客户输入的商品是否存在
def Goods_Existed(Dict, input_keys):
    if Dict.has_key(input_keys):
        return True
    else:
        print('''\n\t\t\t你选择的商品不存在，请重新输入！''')

#用于设置标志位
def BreakFlag():
    while True:
        Break_Flag = input('''\t\t是否继续?(y/n)''')
        if Break_Flag == 'y' or Break_Flag == 'n':
            return True
        else:
            print('''\n\t\t\t您选则的商品不存在，请重新输入!''')

#用于退出系统
def ExitSystem():
    for i in range(3):
        print('''\n\t\t\t\033[34;5m谢谢使用电子商城购物系统，%s秒后，退出系统\033[0m'''%(3-i))
        time.sleep(1)
    exit()

Shopping_Cart = {}
Goods_List = {'iPad':3500, 'Kindle':899, 'MI Pad':1699, 'iMAC':20000, 'MP3':200}

print('''\n\t\t\t\t\033[31; 5m欢迎来到电子商城\033[0m''')

while True:
    try:
        Total_Salary = int(input('''\t\t请输入您的工资：'''))
        if Total_Salary > 899:
            Balance = Total_Salary
            break
        else:
            print('''\t\t\033[31;1m这不是穷B该来的地方!!!\033[0m''')
    except ValueError:#判断是否随意输入字符，若输入不为数字则进行提示，并重新输入
        print('''\t\t\033[31;1m输入错误，请输入数值！\033[0m''')

while True:
    Break_Flag = ''
    print('''\n\t请选择您需要进行的操作：\n\t\t\t\t1.购物\n\t\t\t\t2.查看并修改购物车\n\t\t\t\t3.结账或退出''')
    while True:
        try:
            Choose = int(input('''\t\t请输入您的选择:'''))
        except ValueErrot: #若输入数量不为整形，那么打印输入错误字段
            print('''\n\t\t\t您的输入有误，请重新输入，谢谢!\n''')
            continue
        if Choose >= 4 or Choose <= 0:
            print('''\n\t\t\t您的输入有误，请重新输入，谢谢!''')
        else:
            break
    if Choose == 1:
        while Break_Flag != 'n':
            DicTra(Goods_List)
            Choose_Goods = input('''\t\t亲输入您要购买的商品:''')
            if Goods_Existed(Goods_List,Choose_Goods):
                #判断输入商品是否在商品列表中，若在商品列表，继续执行后续步骤
                if Balance - int(Goods_list[Choose_Goods]) <0:
                    #判断余额是否还能购买商品，若余额不足，显示
                    print('''\n\t\t\t\033[31;1m对不起，您的余额不足！\033[0m\n''')
                    Break_Flag = BreakFlag()
                else:
                    Balance -= int(Goods_List[Choose_Goods])
                    #将总钱数减去商品价格，得到剩余钱数
                    if Shopping_Cart.has_key(Choose_Goods):
                        #判断购物车中是否存在需要购买的商品,有则叠加，没有则添加
                        Shopping_Cart[Choose_Goods][0] += 1
                        Shopping_Cart[Choose_Goods][1] += int(Goods_List[Choose_Goods])
                    else:
                        Shopping_Cart[Choose_Goods] = [1, Goods_List[Choose_Goods]]
                    DicTra(Shopping_Cart)
                    Break_Flag = BreakFlag()
            else:
                Break_Flag = BreakFlag()
    elif Choose == 2:
        DicTra(Shopping_Cart)
        while True:
            try:
                Shopping_Cart_Choose = int(input('''\n\t\t\t\t1.增加\n\t\t\t\t2.减少\n\t\t\t\t3.结账\n\t\t\t\t4.返回\n\t\t请选择您需要进行的操作:'''))
            except ValueError:
                print('''\n\t\t\t您的输入有误，请重新输入，谢谢!\n''')
                continue
            if Shopping_Cart_Choose >= 5 or Shopping_Cart_Choose <= 0:
                print('''\n\t\t\t您的输入有误，请重新输入，谢谢!\n''')
            else:
                break
        if Shopping_Cart_Choose == 1:
            while Break_Flag != 'n':
                DicTra(Shopping_Cart)
                if Shopping_Cart:
                    Shoppong_Cart_Modify = input('''\n\t\t请输入您要增加的商品:''')
                    if Goods_Existed(Shopping_Cart,Shoppong_Cart_Modify):
                        #判断购物车中是否存在需要增加的商品，若有，则增加商品，没有则返回
                            while Break_Flag != 'n':
                                try:
                                    Modify_Time = int(input('''\n\t\t请输入您需要增加的数量:'''))
                                    Surplus_Goods = Shoppong_Cart[Shopping_Cart_Modify][0] + Modify_Times #计算该商品增加数量
                                    Balance -= int(Goods_List[Shopping_Cart_Modify]) * Modify_Times
                                except ValueError:#若输入数量不为整形，那么打印错误字段
                                    print('''\n\t\t\t您输入有误，请重新输入，谢谢！\n''')
                                    continue
                                if Balance < 0:
                                    print('''\n\t\t\t\033[31;1m对不起,你的余额不足！\033[0m\n''')
                                    Blance += int(Goods_List[Shoppong_Cart_Modify[) * Modify_Times
                                    break
                                else:
                                    Shopping_Cart[Shopping_Cart_Modify][0] = Surplus_Goods
                                    Shoppong_Cart[Shoppong_Cart_Modify][1] = int(Goods_List[Shopping_Cart_Modify]) * Surplus_Goods
                                    DicTra(Shopping_Cart)
                                    break
                        else:
                            Break_Flag = BreakFlag()
                    else:
                        Break_Flag = BreakFlag()
            elif Shopping_Cart_Choose == 2:
                while Break_Flag != 'n':
                    DicTra(Shopping_Cart)
                    if Shopping_Cart:
                        break

if __name__ == '__main__':
    #获取月工资
    salary = get_customer_salary()
    total_money = salary
    #初始化购物车
    shopping_cart = []
    while True:
        #打印购物列表
        show_shoppong_list()
        #判断剩余资金是否能购买购物列表中的最低价商品
        if still_can_something(total_money):
            #获取用户需要购买的商品编号
            selection = get_customer_selection()
            #获取此商品价格
            product_price = get_product_price(selection)
            #获取此商品名称
            product_price = get_product_price(selection)
            #判断剩余资金是否购买商品
            if total_money >= product_price:
                total_money -= product_price
                #打印购买成功信息
                print("Congratutlations! you bought a %s successfully!\n" %product_name)
                #将商品加入购物车
                shopping_cart.append(product_name)
                #打印剩余资金
                print("you still have %d RMB left\n" %total_money)
                #判断是否还想购买其他商品
                if not still_want_to_buy_something():
                    print("thank you for coming!")
                    break
            else:
                #输出还需要工作多久才能购买
                format_time = time_needed_to_work_for_buying_products(salary, product_price-total_money)
                print("sorry you can not afford this product!\n")
                print("you have to work '%s' to get it! \n"%format_time)
                #判断是否还想购买其它商品
                if not still_want_to_buy_something():break
        else:
            #输出提示你已经无法负担任何商品
            print("sorry, you do not have enough money to purchase anything!\n")
            break
    #打印购物车列表
    print("you bought %s"%shopping_cart)

















