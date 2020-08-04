#people类
class Person(object):
    def __init__(self, name, age, sex):
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
        return self.sex

    def __str__(self):
        return "%s %d %s" % (self.name, self.age, self.sex)
