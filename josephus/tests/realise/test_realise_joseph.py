from josephus.realise.realise_joseph import RealiseJoseph


def test_joseph():
    file = "E:/git/Python-learning/josephus/file/people.txt"
    start = 2
    step = 5
    joseph = RealiseJoseph(file, start, step)
    print(joseph.get_str_result())
