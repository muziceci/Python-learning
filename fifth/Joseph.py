#实现约瑟夫环类
import Reader
import People

class Joseph:
    def __init__(self, start, step):
        self._people = []
        self._kill_people = []
        self.start = start
        self.step = step
        self.current = start - 1
    
    def append(self, people_lst):
        for i in people_lst:
            self._people.append(People.Person(i[0], int(i[1]), int(i[2])))

    def creat_people_from_txt(self, file):
        people_lst = Reader.txt_reader(file)
        self.append(people_lst)
    
    def creat_people_from_csv(self, file):
        people_lst = Reader.csv_reader(file)
        self.append(people_lst)

    def creat_people_from_zip(self, file):
        people_lst = Reader.zip_reader(file)
        self.append(people_lst)

    def get_pop_order(self, people_lst, current_index):
        num = len(people_lst)
        current_index = (current_index + self.step - 1) % num
        return current_index

    def pop(self, current):
        return self._people.pop(current)

    def get_survive_person(self):
        return self._people[0]

    def __iter__(self):
        current = self.current
        while len(self._people) > 1:
            current = self.get_pop_order(self._people, current)
            yield self.pop(current)

