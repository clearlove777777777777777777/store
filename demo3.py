class people:
    age = 0
    sex = ''
    name = ''
    # def __init__(self, a, s, n ):
    #     self.age = a
    #     self.sex = s
    #     self. name = n
    def GH(self):
        print(self.name, "干活")


class Gpeople(people):
    def GH(self):
        super(Gpeople, self).GH()


class student(Gpeople):
    xh = 0

    def study(self):
        print(self.name, '正在学习')

    def sing(self):
        print(self.name, '正在唱歌')

people.name = 'ww'
people.sex = 'nm'
people.age = 10

d = people()
b = Gpeople()
c = student()


c.study()
c.sing()