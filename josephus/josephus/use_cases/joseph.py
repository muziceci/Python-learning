# 实现约瑟夫环类
from josephus.entity.person import Person


class Joseph:
    def __init__(self, start: int, step: int):
        # 初始化
        self.people: list = []
        self.kill_people: list = []
        self.start = start
        self.step = step
        self.current = start - 1

    def append(self, lst: list) -> None:
        # 添加元素
        for i in lst:
            self.people.append(i)

    def get_len(self) -> int:
        # 获取约瑟夫环长度
        return len(self.people)

    def pop(self, current: int) -> Person:
        return self.people.pop(current)

    def __iter__(self):
        return self

    def __next__(self):
        # 迭代
        if self.get_len() < 2:
            raise StopIteration
        self.current = (self.current + self.step - 1) % len(self.people)
        person = self.pop(self.current)
        return person

    def get_survive(self):
        # 获取最后留下的
        return self.people[0]


