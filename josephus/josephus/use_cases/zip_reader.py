import zipfile
from josephus.entity.reader import Reader
from josephus.entity.person import Person


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
