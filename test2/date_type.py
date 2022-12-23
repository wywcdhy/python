"""
python一共有
"""
from operator import add


class Animal:
    @staticmethod
    def life():
        print("Animal life is true")


class Tiger(Animal):
    @staticmethod
    def eat():
        print("Tiger like eat meat")


class Student(object):
    @property
    def score1(self):
        return self.__score

    @score1.setter
    def score3(self, value):
        if value > 100:
            value = 100
        if value < 0:
            value = 0
        self.__score = value


"""
调用score3函数,将值赋值给self.__score,s.score1读取self.__score的值
"""

# coding: utf-8
from enum import Enum, unique


@unique
class Month(Enum):
    Jan = 0
    Feb = 1
    Mar = 2


# coding: utf-8
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, base, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        # 打印参数信息
        print(cls, '\n', name, '\n', base, '\n', attrs, '\n')
        return type.__new__(cls, name, base, attrs)


# 根据metaclass产生类
class MyList(list, metaclass=ListMetaclass):
    pass


# 类继承
class OtherList(MyList):
    pass



if __name__ == '__main__':
    tiger = Tiger()
    tiger.life()
    tiger.eat()
    Tiger.life()
    s = Student()
    s.score3 = 999
    print(s.score1)
    # month = Month()
    # Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    # # 可以直接使用Month.Jan来引用一个常量：
    # print(Month.Jan.value)
    # 枚举所有成员：
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)


    # 定义成员方法：减
    def sub(self, x, y):
        return x - y


    # 生成类
    Hello = type('Hello', (object,), {"add": add, "mysub": sub})
    h = Hello()
    print(h.add(1, 2))
    print(h.mysub(1, 2))
    print(type(h))
    print(type(Hello))
    L = MyList()
    L.add('3')
    print(L)
