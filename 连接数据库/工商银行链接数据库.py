import random
import datetime
from DBUtils import select
from DBUtils import update


print("*******************************************")
print("*               中国工商银行                *")
print("*               账户管理系统                *")
print("*                  v1.0                   *")
print("*******************************************")
print("                                           ")
print("* 1.开户                                   *")
print("* 2.存钱                                   *")
print("* 3.取钱                                   *")
print("* 4.转账                                   *")
print("* 5.查询                                   *")
print("* 6.Bye                                   *")
print("*******************************************")


bank = {}
bank_name = "工商银行七马路分行"


def bank_adduser(account, username, password, country, province, street, door, money, registerDate, bank_name):
    sql = 'select count(*) from jarvis'
    param = []
    data = select(sql, param)
    if len(data) >= 100:
        return 3

    sql1 = 'select * from jarvis where username = %s'
    param1 = [username]
    data = select(sql1, param1)
    if len(data) > 0:
        return 2

    sql2 = 'insert into jarvis values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    param2 = [account, username, password, country, province, street, door, money, registerDate, bank_name]
    update(sql2, param2)
    return 1


def adduser():
    # 注册
    account = random.randint(10000000, 99999999)
    username = input("请输入您的姓名")
    password = int(input("请输入您的密码"))
    country = input("请输入您的国家")
    province = input("\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t\t请输入您的门牌号")
    money = 0
    registerDate = datetime.datetime.now()
    bank_name = "工商银行七马路分行"

    status = bank_adduser(account, username, password, country, province, street, door, money, registerDate, bank_name)
    if status == 1:
        print("恭喜您开户成功下面是你的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：******
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''

        print(info % (username, account, country, province, street, door, money, bank_name))
    elif status == 2:
        print('用户已存在')
    elif status == 3:
        print('用户库已满')


def usermoney():
    # 登录
    username = input('请输入您的用户名')
    sql = "select * from jarvis where username = %s"
    param = [username]
    name = select(sql, param)
    if len(name) != 0:
        password = input('请输入您的密码')
        sql1 = 'select password from jarvis where username = %s'
        param1 = [username]
        word = select(sql1, param1, mode='one')[0]
        print(word)
        print(password)
        if word != password:
            print('密码输入错误')
        else:
            a = int(input('请输入您的取款金额'))
            sql2 = 'select money from jarvis where username = %s'
            mon = select(sql2, param, mode='one')[0]
            if a > mon:
                print('余额不足')
            else:
                sql3 = 'UPDATE jarvis SET money = money - %s  WHERE username = %s'
                param3 = [a, username]
                update(sql3, param3)
    else:
        print('账号不存在')


def amunt():
    username = input('请输入您的用户名')
    sql = "select * from jarvis where username = %s"
    param = [username]
    name = select(sql, param)
    if len(name) == 0:
        print('用户名输入错误')
    else:
        amun = int(input('请输入您要存入的金额'))
        sql = "UPDATE jarvis SET money = money + %s  WHERE username = %s"
        param = [amun, username]
        update(sql, param)


def transfer():

    username1 = input('请输入付款用户名')
    username2 = input('请输入收款用户名')
    sql = "select * from jarvis where username = %s"
    param = [username1]
    sql2 = "select * from jarvis where username = %s"
    param2 = [username2]
    z = select(sql, param)
    x = select(sql2, param2)
    if len(z) != 0 and len(x) != 0 and z != x:
            password = input('请输入付款账号密码')
            sql3 = "select password from jarvis where username = %s"
            param3 = [username1]
            c = select(sql3, param3, mode='one')[0]
            if password != c:
                print('密码错误')
            else:
                    transfer_money = int(input('请输入转账金额'))
                    sql4 = "select money from jarvis where username = %s"
                    param4 = [username1]
                    v = select(sql4, param4, mode='one')[0]
                    if transfer_money > v:
                        print('余额不足')
                    else:
                        sql5 = "UPDATE jarvis SET money = money - %s  WHERE username = %s"
                        param5 = [transfer_money, username1]
                        update(sql5, param5)
                        sql6 = "UPDATE jarvis SET money = money + %s  WHERE username = %s"
                        param6 = [transfer_money, username2]
                        update(sql6, param6)



def search():
    username = input('请输入用户名')
    password = input('请输入密码')
    sql = "select * from jarvis where username = %s"
    param = [username]
    b = select(sql, param)
    sql2 = "select password from jarvis where username = %s"
    param2 = [username]
    n = select(sql2, param2)
    if len(b) != 0:
        if password != n:
            print(b)
        else:
            print('密码错误')
    else:
        print('用户名错误')


m = True
while m:
    begin = input("请选择业务")
    if begin == "1":
        print("1、开户")
        adduser()
    #     添加用户
    elif begin == "2":
        print("2、取钱")
        usermoney()
    #     登陆取款
    elif begin == "3":
        print("3、存钱")
        amunt()
    #     存款
    elif begin == "4":
        print("4、转账")
        transfer()
    #     转账
    elif begin == "5":
        print("5、查询 ")
        search()
    #     查询
    elif begin == "6":
        m = False
        print("6、您已退出系统欢迎下次再来")
