import csv
import zipfile

class Reader(object):
    def __init__(self, file):
        self.file = file
    def reader(self):
        print("这是父类的方法")
    def test(self):
        print("这是测试方法！")

class txt_reader(Reader):
    # def __init__(self):
        # super.__init__()
    def reader(self):
        print("这是子类的方法,输出父类的参数：", self.file)


a = Reader("peopler.txt")
a.reader()
print("====================")
b = txt_reader("people.txt")
b.file = "people.txt"
b.reader()
print("====================")
b.test()


