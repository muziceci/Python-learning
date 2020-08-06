import csv
import json
import zipfile
from josephus.entity.reader import Reader
from josephus.entity.person import Person


class CsvReader(Reader):
    def reader(self) -> list:
        lst = []
        with open(self.file, 'r') as csv_file:
            reader = csv.reader(csv_file)  #调用csv的reader（）函数
            for i in reader:
                lst.append(Person(i[0], int(i[1]), int(i[2])))
        return lst


class TxtReader(Reader):
    def reader(self) -> list:
        people_lst = []
        with open(self.file, 'r') as people:
            for i in people:
                obj = json.loads(i, object_hook=self.person_decoder)
                people_lst.append(obj)
        return people_lst

    def person_decoder(self, dct) -> Person:
        return Person(dct["name"], dct["age"], dct["sex"])


class ZipReader(Reader):
    def reader(self) -> list:
        people_lst = []
        with zipfile.ZipFile(self.file, 'r') as zip_file:   #解压zip文件
            content = []
            for i in zip_file.namelist():
                content += zip_file.open(i).readlines()  #打开zip里面的文件，遍历每个文件并逐行读取
            for j in content:
                lst = j.decode('UTF-8').split(',')
                people_lst.append(Person(lst[0], int(lst[1]), int(lst[2])))   #bytes转化为str
        return people_lst


