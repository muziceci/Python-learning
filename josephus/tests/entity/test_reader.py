from josephus.entity.reader import Reader


def test_reader():
    file = ""
    reader = Reader(file)
    assert reader.file == ""

