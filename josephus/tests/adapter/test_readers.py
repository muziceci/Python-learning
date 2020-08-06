from josephus.adapter.readers import TxtReader, CsvReader, ZipReader
TXT_FILE = "E:/git/Python-learning/josephus/file/people.txt"
CSV_FILE = "E:/git/Python-learning/josephus/file/people.csv"
ZIP_FILE = "E:/git/Python-learning/josephus/file/people.zip"


class TestReader:
    def test_txt_reader(self):
        txt = TxtReader(TXT_FILE)
        result = txt.reader()
        assert len(result) == 8

    def test_zip_reader(self):
        zip = ZipReader(ZIP_FILE)
        result = zip.reader()
        assert len(result) == 11

    def test_csv_reader(self):
        csv = CsvReader(CSV_FILE)
        result = csv.reader()
        assert len(result) == 6

