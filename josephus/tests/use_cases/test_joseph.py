from josephus.use_cases.joseph import Joseph
from josephus.entity.person import Person


def test_append():
    Jack = Person("Jack", 15, 1)
    joseph = Joseph(2, 2)
    joseph.append(Jack)
    assert isinstance(joseph.pop(0), Person)


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

