import random


def max(x, y):
    if x >= 1000 | x <= 2000:
        y = y + x + (y+x)*0.1
        return y
    elif x >= 2000:
        y = y + x + (y+x)*0.2
        return y


ret = 0
while ret == 0:
    a, b, mon = 0, 0, 0
    # a是循环控制值，b是充值金额，mon是账户余额
    print("===========================================")
    print("$       *    欢迎光临无良游戏       *        j")
    print("$   *   *      *         *     *        * a")
    print("$   *     *   开始游戏请”1“     *     *     r")
    print("$ *    *      *       *        *       *  v")
    print("$   *     *   退出游戏按”Q“      *      *   i")
    print("==========================================s")
    star = input("是否开始游戏")
    if star == "1":
        b = int(input("请输入充值金额"))
        mon = max(b, mon)
        run = random.randint(20, 90)
        print(mon)
        while a < 5:
            a += 1
            mon -= 500
            num = int(input("请输入一个数字"))
            if num == run:
                print("ok")
                break
            elif num > run:
                print("你猜大了")
            elif num < run:
                print("你猜小了")
            elif mon == 0:
                break
    elif star != "Q" and star != 1:
        ret = 0
        print("再给你一个输入“1”的机会")
    elif star == "Q":
        print("再见来不及挥手")
        break
