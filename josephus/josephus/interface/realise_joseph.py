import json
import os
from josephus.use_cases.joseph import Joseph
from josephus.adapter.readers import CsvReader, TxtReader, ZipReader


class RealiseJoseph:
    def __init__(self, file: str, start: int, step: int):
        self.file = file
        self.start = start
        self.step = step

    def get_people_lst(self, file) -> list:
        if file == ' ':
            raise ValueError
        elif os.path.exists(file):
            lst = []
            file = self.file
            if file.endswith('.txt'):
                txt_reader = TxtReader(file)
                lst = txt_reader.reader()
            elif file.endswith('.csv'):
                csv_reader = CsvReader(file)
                lst = csv_reader.reader()
            elif file.endswith('.zip'):
                zip_reader = ZipReader(file)
                lst = zip_reader.reader()
            return lst
        else:
            raise FileNotFoundError

    def create_joseph(self):
        # 判断开始的值和步长是否符合要求
        people_lst = self.get_people_lst(self.file)
        joseph_len = len(people_lst)
        if self.start < 1 or self.start > joseph_len:
            raise ValueError("The value of start cannot be under 1 or over the length of people list!")
        elif self.step > joseph_len or self.step < 1:
            raise ValueError("The value of step cannot be under 1 or over the length of people list!")
        joseph = Joseph(self.start, self.step)
        joseph.append(people_lst)
        return joseph

    def get_result(self):
        joseph = self.create_joseph()
        kill_lst = []
        for i in joseph:
            kill_lst.append(str(i))
        str_kill = json.dumps(kill_lst, ensure_ascii=False, indent=0)

        remain_result = joseph.get_survive()
        str_remain = str(remain_result)

        result = '被杀的次序:' + str_kill + '\n' + '最后留下的人:' + '\n' + str_remain
        return result.replace('[', ' ').replace(']', ' ').replace('"', ' ').replace(',', ' ')

