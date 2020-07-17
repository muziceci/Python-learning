#people类
class Person(object):
    def __init__(self, name, age, sex=0):
        self.name = name
        self.age = age
        self.sex = sex

    @property
    def get_name(self):
        return self.name

    @property
    def get_age(self):
        return self.age

    @property
    def get_sex(self):
        if self.sex == 0:
            return 'Female'
        else:
            return 'Male'

    def __str__(self):
        return "姓名：%s 年龄：%d 性别：%s"%(self.name, self.age, self.get_sex)
