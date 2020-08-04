from josephus.use_cases.txt_reader import TxtReader


def test_txt_reader():
    txt = TxtReader("E:/git/Python-learning/josephus/file/people.txt")
    result = txt.reader()
    assert (len(result) == 8)

