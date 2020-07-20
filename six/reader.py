
import csv
import sys
import zipfile

class Reader(object):
    def __init__(self, file):
        self.file = file
    def reader(self):
        pass

class txt_reader(Reader):
    def reader(self):
        try:
            with open(self.file, 'r') as people:
                lst = [i.split(',') for i in people]
            return lst
        except FileNotFoundError:
            print("File is not found")
            sys.exit(0)
        except PermissionError:
            print("You don't have permission to access this file.")

class csv_reader(Reader):
    def reader(self):
        lst = []
        try:
            with open(self.file, 'r') as csv_file:
                reader = csv.reader(csv_file)  #调用csv的reader（）函数
                for i in reader:
                    lst.append(i)
                return lst
        except FileNotFoundError:
            print("File is not found")
            sys.exit(0)
        except PermissionError:
            print("You don't have permission to access this file.")

class zip_reader(Reader):
    def reader(self):
        lst = []
        try:
            with zipfile.ZipFile(self.file, 'r') as zip_file:   #解压zip文件
                content = []
                for i in zip_file.namelist():
                    content += zip_file.open(i).readlines()  #打开zip里面的文件，遍历每个文件并逐行读取
                for j in content:
                    lst.append(j.decode('UTF-8').split(','))   #bytes转化为str
                    # lst.append(i.decode('ascii').split(','))   #bytes转化为str
                return lst
        except FileNotFoundError:
            print("File is not found")
            sys.exit(0)
        except PermissionError:
            print("You don't have permission to access this file.")

        
#测试方法
def test_txt_reader():
    test = txt_reader("people.txt")
    txt_lst = test.reader()
    assert(len(txt_lst) == 8)
    print("测试txt_reader")
    print(txt_lst)

def error_test_txt_reader():
    test = txt_reader("people.txt")
    txt_lst = test.reader()
    assert(len(txt_lst) == 9)
    print("测试txt_reader")
    print(txt_lst)

def test_csv_reader():
    test = csv_reader("people.csv")
    csv_lst = test.reader()
    assert(len(csv_lst) == 8)
    print("测试csv_reader")
    print(csv_lst)

def test_zip_reader():
    test = zip_reader("people.zip")
    zip_lst = test.reader()
    assert(len(zip_lst) == 11)
    print("测试zip_reader")
    print(zip_lst)

if __name__ == "__main__":
    # test_csv_reader()
    # error_test_txt_reader()
    # test_txt_reader()
    test_zip_reader()
