import json
from josephus.entity.reader import Reader
from josephus.entity.person import Person


class TxtReader(Reader):
    def reader(self) -> list:
        people_lst = []
        with open(self.file, 'r') as people:
            for i in people:
                obj = json.loads(i, object_hook=self.decoder)
                people_lst.append(obj)
        return people_lst

    def decoder(self, dct) -> Person:
        return Person(dct["name"], dct["age"], dct["sex"])


