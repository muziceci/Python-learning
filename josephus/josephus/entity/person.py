#people类
class Person(object):
    def __init__(self, name: str, age: int = 1, sex: int = 0):
        self.name = name
        if age > 0:
            self.age = age
        else:
            raise ValueError("输入的年龄必须小于0！")

        if sex == 0:
            self.sex = 'Female'
        else:
            self.sex = 'Male'

    def __str__(self):
        return "姓名：%s 年龄：%d 性别：%s" % (self.name, self.age, self.sex)
