
import os
import csv
import zipfile

class Reader(object):
    ext = None
    def __init__(self, file):
        self.file = file
    def reader(self):
        pass
#ext是类属性，这一类共有的属性，不存在存在对象才能存在
#对象属性
class TxtReader(Reader):
    # ext = "txt"
    def reader(self):
        with open(self.file, 'r') as people:
            lst = [i.split(',') for i in people]
        return lst

class CsvReader(Reader):
    # ext = "txt"
    def reader(self):
        lst = []
        with open(self.file, 'r') as csv_file:
            reader = csv.reader(csv_file)  #调用csv的reader（）函数
            for i in reader:
                lst.append(i)
            return lst

class ZipReader(Reader):
    # ext = "zip"
    def reader(self):
        lst = []
        with zipfile.ZipFile(self.file, 'r') as zip_file:   #解压zip文件
            content = []
            for i in zip_file.namelist():
                content += zip_file.open(i).readlines()  #打开zip里面的文件，遍历每个文件并逐行读取
            for j in content:
                lst.append(j.decode('UTF-8').split(','))   #bytes转化为str
                # lst.append(i.decode('ascii').split(','))   #bytes转化为str
        return lst
      
def get_people_lst_from(file):
    people_lst = []
    if os.path.exists(file):
        if file.endswith('.txt'):
            txt_reader = TxtReader(file)
            people_lst = txt_reader.reader()
        elif file.endswith('.csv'):
            csv_reader = CsvReader(file)
            people_lst = csv_reader.reader()
        elif file.endswith('.zip'):
            zip_reader = ZipReader(file)
            people_lst = zip_reader.reader()
    else:
        # print("File is not found")
        raise FileNotFoundError
    return people_lst

        
#测试方法
def test_txt_reader():
    txt_reader = TxtReader("people.txt")
    txt_lst = txt_reader.reader()
    assert(len(txt_lst) == 8)
    print("测试txt_reader")
    print(txt_lst)

def error_test_txt_reader():
    txt_reader = TxtReader("people.txt")
    txt_lst = txt_reader.reader()
    assert(len(txt_lst) == 9)
    print("测试txt_reader")
    print(txt_lst)

def test_csv_reader():
    csv_reader = CsvReader("people.csv")
    csv_lst = csv_reader.reader()
    assert(len(csv_lst) == 8)
    print("测试csv_reader")
    print(csv_lst)

def test_zip_reader():
    zip_reader = ZipReader("people.zip")
    zip_lst = zip_reader.reader()
    assert(len(zip_lst) == 11)
    print("测试zip_reader")
    print(zip_lst)

if __name__ == "__main__":
    # test_csv_reader()
    # error_test_txt_reader()
    # test_txt_reader()
    test_zip_reader()
    
