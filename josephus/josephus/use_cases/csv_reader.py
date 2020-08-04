import csv
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
