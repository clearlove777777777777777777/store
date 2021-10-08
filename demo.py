from threading import Thread
import time

box = 0
# 蛋挞盒子

class chef(Thread):
    chefname = ''
    count = 0
    def run(self) -> None:
        global box
        while True:
            if box < 500:
                box = box + 1
                print('盒子里有', box, '个蛋挞')
                time.sleep(0.1)
                self.count += 1
            elif box == 500:
                time.sleep(3)
                print(self.chefname, "做了", self.count, '蛋挞')
                time.sleep(0.1)
                break



class shopper (Thread):
    shoppername = ''
    count1 = 0
    money = 300
    def run(self) -> None:
        global box
        while True:
            if self.money > 0:
                if box > 0:
                    box = box - 1
                    self.money -= 2
                    print(self.shoppername, '买了一个蛋挞')
                    print(self.shoppername, '还剩', self.money, '元')
                    time.sleep(0.1)
                    self.count1 += 1
                else:
                    time.sleep(3)
            else:
                print("买了", self.count1, '个蛋挞')
                break


a1 = chef()
a2 = chef()
a3 = chef()
b1 = shopper()
b2 = shopper()
b3 = shopper()
b4 = shopper()
b5 = shopper()
b6 = shopper()

a1.chefname = '小耗子'
a2.chefname = '小皓子'
a3.chefname = '小白告子'


b1.shoppername = '小小怪下士'
b2.shoppername = '大大怪下士'
b3.shoppername = '大小怪下士'
b4.shoppername = '上上怪下士'
b5.shoppername = '下下怪下士'
b6.shoppername = '左右怪下士'

a3.start()
a2.start()
a1.start()
b1.start()
b2.start()
b3.start()
b6.start()
b5.start()
b4.start()

