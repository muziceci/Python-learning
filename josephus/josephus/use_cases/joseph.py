# 实现约瑟夫环类
from josephus.entity.person import Person


class Joseph:
    def __init__(self, start: int, step: int):
        self._people: list = []
        self._kill_people: list = []
        self.start = start
        self.step = step
        self.current = start - 1

    def append(self, person: Person):
            self._people.append(person)

    def get_len(self):
        return len(self._people)

    def get_pop_order(self, people_lst: list, current_index: int) -> int:
        num = len(people_lst)
        current_index = (current_index + self.step - 1) % num
        return current_index

    def pop(self, current: int) -> Person:
        return self._people.pop(current)

    def get_survive_person(self) -> Person:
        return self._people[0]

    def __iter__(self):
        current = self.current
        while len(self._people) > 1:
            current = self.get_pop_order(self._people, current)
            yield self.pop(current)



