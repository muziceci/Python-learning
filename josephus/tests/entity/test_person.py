from josephus.entity.person import Person


class TestPerson:
    def test_get_name(self):
        person = Person("jack")
        assert(person.name == "jack")

    def test_get_age(self):
        person = Person("jack", age=15)
        assert(person.age == 15)

    def test_error_age(self):
        person = Person("jack", age=-1)
        assert(person.age == -1)

    def test_get_sex(self):
        person = Person("jack", sex=1)
        assert(person.sex == 'Male')

    def test_str(self):
        person = Person("jack", age=19, sex=1)
        assert(str(person) == "姓名：jack 年龄：19 性别：Male")
