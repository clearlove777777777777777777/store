class oldPhone:
    __PP = ''

    def setPP(self, PP):
        self.__PP = PP

    def getPP(self):
        return self.__PP

    def call(self, phoneNumber):
        print('正在给', phoneNumber, '打电话')

    def PP(self):
        print('品牌为', self.__PP, '的手机很好用')


class NewPhone (oldPhone):
    def call(self, phoneNumber):
        print('语音拨号中。。。。。')
        super().call(phoneNumber)

    def PP(self):
        super().PP()


b = NewPhone()
b.call(1000000000)
b.setPP('121212')
b.PP()

