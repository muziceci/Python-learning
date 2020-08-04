from josephus.interface.get_people_lst import get_people_lst_from
from josephus.entity.person import Person


def test_get_people_lst():
    people_lst = get_people_lst_from("E:/git/Python-learning/josephus/file/people.zip")
    assert isinstance(people_lst, list)
    assert isinstance(people_lst[0], Person)
