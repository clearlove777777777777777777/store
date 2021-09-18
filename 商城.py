import random


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
bank_name = "无良银行私人银行"


def bank_adduser(account, username, password, country, province, street, door):
    if len(bank) > 100:
        return 3
    if username in bank:
        return 2
    bank[username] = {
        "username": username,
        "account": account,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money": 0,
        "bank_name": bank_name
    }
    print(bank)
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

    status = bank_adduser(account, username, password, country, province, street, door)
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

        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
    elif status == 2:
        print('用户已存在')
    elif status == 3:
        print('用户库已满')


def deposit():    # 存钱登录
    adduser = input("请输入您的帐户")
    if adduser not in bank:
        return False
    else:
        amunt = int(input("请输入存款金额"))
    money = bank[adduser]["money"]
    money = money + amunt
    bank[adduser]["money"] = money

    print("您的余额为：", bank[adduser]["money"])


def withdrawal():
    qk = input("请输入您的账号")
    qkje = int(input("请输入取款金额"))
    if qk not in bank:
        return 1
    else:
        qkpassword = int(input("请输入您的取款密码"))
        if qkpassword != bank[qk]["password"]:
            return 2
        else:
            if qkje <= bank[qk]["money"]:
                bank[qk]["money"] = bank[qk]["money"] - qkje
                print("您的账户余额为：", bank[qk]["money"])
            elif qkje > bank[qk]["money"]:
                return 3


def transfer():
    zz1 = input("请输入转账账号")
    zz2 = input("请输入收款账号")
    if zz1 and zz2 not in bank:
        return 1
    else:
        zzpassword = int(input("请输入您的账户密码"))
        if zzpassword != bank[zz1]["password"]:
            return 2
        else:
            zzje = int(input("请输入转账金额"))
            if zzje > bank[zz1]["money"]:
                return 3
            elif zzje <= bank[zz1]["money"]:
                bank[zz1]["money"] = bank[zz1]["money"] - zzje
                bank[zz2]["money"] = bank[zz2]["money"] + zzje


def query():
    cxzh = input("请输入查询的账户")
    if cxzh not in bank:
        print("该用户不存在")
    else:
        cxpassword = int(input("请输入查询账户的密码"))
        if cxpassword != bank[cxzh]["password"]:
            print("密码输入错误")
        else:
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

            print(info % (bank[cxzh]["username"], bank[cxzh]["account"], bank[cxzh]["country"], bank[cxzh]["province"],
                          bank[cxzh]["street"], bank[cxzh]["door"], bank[cxzh]["money"], bank_name))


select = True
while select:
    begin = input("请选择业务")
    if begin == "1":
        print("1、开户")
        adduser()
    #     添加用户
    elif begin == "2":
        print("2、取钱")
        withdrawal()
    #     登陆取款
    elif begin == "3":
        print("3、存钱")
        deposit()
    #     存款
    elif begin == "4":
        print("4、转账")
        transfer()
    #     转账
    elif begin == "5":
        print("5、查询 ")
        query()
    #     查询
    elif begin == "6":
        select = False
        print("6、您已退出系统欢迎下次再来")