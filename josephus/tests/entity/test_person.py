import pytest
from josephus.entity.person import Person


class TestPerson:
    def test_init_and_str(self):
        person = Person("jack", 17, 0)
        assert person.name == "jack"
        assert person.age == 17
        assert person.sex == "Female"
        assert str(person) == "姓名：jack 年龄：17 性别：Female"

    def test_age_error(self):
        with pytest.raises(ValueError) as ve:
            person = Person("jack", -1)
            assert str(ve.value) == "The age must be under zero！"

