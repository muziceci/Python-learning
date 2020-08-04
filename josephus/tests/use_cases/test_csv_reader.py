from josephus.use_cases.csv_reader import CsvReader


def test_csv_reader():
    csv = CsvReader("E:/git/Python-learning/josephus/file/people.csv")
    result = csv.reader()
    assert (len(result) == 6)

