#实现约瑟夫环类


import people

class Joseph:
    def __init__(self, start, step):
        self._people = []
        self._kill_people = []
        self.start = start
        self.step = step
        self.current = start - 1

    def append(self, people_lst):
        for i in people_lst:
            self._people.append(people.Person(i[0], int(i[1]), int(i[2])))

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
            
def test_joseph_iter():
    Jack = ["Jack", 15, 1]
    Mark = ["Mark", 17, 1]
    Helle = ["Helle", 18, 0]
    people_lst = [Jack, Mark, Helle]
    joseph = Joseph(2, 2)
    joseph.append(people_lst)
    print("被杀掉的依次是：")
    for i in joseph:
        print(i)

if __name__ == "__main__":
    test_joseph_iter()