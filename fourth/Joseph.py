#实现约瑟夫环类
class Joseph(object):
    def __init__(self):
        self._people = []
        self.kill = []
        self.step = 0
        self.current_num = 0

    def set_step(self, step):
        self.step = step

    def append(self, person):
        self._people.append(person)

    def get_survive_number(self):
        joseph_lst = self._people
        kill_lst = self.kill
        length = len(self._people)
        temp = 1  #计数
        index = 0 #元素下标
        while len(joseph_lst) > 1:
            if temp == self.step:
                kill_lst.append(joseph_lst[index])
                joseph_lst.pop(index)
                temp = 1
            else:
                temp += 1
                index += 1
            if index == length-len(kill_lst):
                index = 0
        return joseph_lst[0]

    def next(self):       #迭代
        if self.current_num < len(self._people):
            person = self._people[self.current_num]
            self.current_num += 1
            return person
        else:
            raise StopIteration()