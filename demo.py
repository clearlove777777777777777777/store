class oldche:
    __name = ''
    __age = 0

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def setage(self):
        self.__age = 100

    def getage(self):
        return self.__age

    def cook(self):
        print(self.getname(), "在蒸cookie")

    def chao(self):
        print(self.getname(), '正在炒菜')


class newchef(oldche):
    def chao(self):
        super().chao()


class new1chef(newchef):

    def chao(self):
        super().chao()

    def cook(self):
        super().cook()

a = oldche()
b = newchef()
c = new1chef()

a.setname('蔚超慧')
b.setname('刘合威')
c.setname('jarvis')
a.cook()
b.chao()
c.chao()


