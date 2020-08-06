import pytest
from josephus.interface.realise_joseph import RealiseJoseph


class TestRealiseJoseph:
    @classmethod
    def setup_method(cls):
        cls.file = "E:/git/Python-learning/josephus/file/people.txt"
        cls.start = 2
        cls.step = 3
        cls.realise_joseph = RealiseJoseph(cls.file, cls.start, cls.step)

    def test_init(self):
        assert self.realise_joseph.file == "E:/git/Python-learning/josephus/file/people.txt"
        assert self.realise_joseph.start == 2
        assert self.realise_joseph.step == 3

    def test_get_people_lst(self):
        assert isinstance(self.realise_joseph.get_people_lst(self.file), list)

    def test_create_joseph(self):
        len = 0
        for i in self.realise_joseph.get_people_lst(self.file):
            len += 1
        under_start = -1
        under_step = -10
        over_start = len+1
        over_step = len+10
        with pytest.raises(ValueError, match="The value of start cannot be under 1 or over the length of people list!"):
            RealiseJoseph(self.file, under_start, self.step).create_joseph()
        with pytest.raises(ValueError, match="The value of start cannot be under 1 or over the length of people list!"):
            RealiseJoseph(self.file, over_start, self.step).create_joseph()
        with pytest.raises(ValueError, match="The value of step cannot be under 1 or over the length of people list!"):
            RealiseJoseph(self.file, self.start, over_step).create_joseph()
        with pytest.raises(ValueError, match="The value of step cannot be under 1 or over the length of people list!"):
            RealiseJoseph(self.file, self.start, under_step).create_joseph()

    def test_get_result(self):
        assert isinstance(self.realise_joseph.get_result(), str)





