import pytest
from collections.abc import Iterable
from josephus.use_cases.joseph import Joseph


class TestJoseph:
    @classmethod
    def setup_method(cls):
        # 在每个方法执行之前执行
        lst = [1, 2, 3]
        cls.joseph = Joseph(2, 2)
        cls.joseph.append(lst)

    def test_init(self):
        assert self.joseph.start == 2
        assert self.joseph.step == 2

    def test_append(self):
        assert self.joseph.people == [1, 2, 3]

    def test_get_len(self):
        assert self.joseph.get_len() == 3

    def test_pop(self):
        assert self.joseph.pop(0) == 1

    def test_joseph_iter(self):
        assert isinstance(self.joseph, Iterable)

    def test_joseph_next(self):
        assert self.joseph.__next__() == 3
        assert self.joseph.__next__() == 2
        with pytest.raises(StopIteration):
            assert self.joseph.__next__() == 1

    def test_get_survive(self):
        assert self.joseph.get_survive() == 1

