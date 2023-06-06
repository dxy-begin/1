# __init__()函数的一种定义方式
# def __init__(self,形参1，形参2):
# 函数里有几个参数，括号里就写几个形参,在实例化的时候，必须把所有参数的值都传进去

class Student:
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为Student绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('大冰', 19)  # 实例化的时候要传两个参数
print(stu.__dict__)  # 输出一下实例化后的属性