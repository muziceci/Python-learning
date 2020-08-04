import json
from josephus.interface import get_people_lst as gpl
from josephus.use_cases.joseph import Joseph


class RealiseJoseph:
    def __init__(self, file: str, start: int, step: int):
        self.file = file
        self.start = start
        self.step = step
        self.joseph = Joseph(start, step)

    def init_joseph(self) -> None:
        people_lst = gpl.get_people_lst_from(self.file)
        for i in people_lst:
            self.joseph.append(i)
        joseph_len = self.joseph.get_len()

        if self.start > joseph_len:
            raise ValueError("start值超出约瑟夫环长度")
        elif self.step > joseph_len:
            raise ValueError("step值超出约瑟夫环长度")

    def get_kill_lst(self) -> str:
        kill_lst = []
        for i in self.joseph:
            kill_lst.append(str(i))
        return json.dumps(kill_lst, ensure_ascii=False, indent=4)

    def remain_result(self):
        try:
            result = self.joseph.get_survive_person()
            return str(result)
        except ValueError as ve:
            print(ve)

    def get_str_result(self) -> str:
        self.init_joseph()
        str_kill = self.get_kill_lst()
        str_remain = self.remain_result()
        return '被杀的次序\n'+str_kill+'\n'+'最后留下的人'+'\n'+str_remain



