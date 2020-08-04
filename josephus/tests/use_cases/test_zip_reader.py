from josephus.use_cases.zip_reader import ZipReader


def test_zip_reader():
    zip = ZipReader("E:/git/Python-learning/josephus/file/people.zip")
    result = zip.reader()
    assert (len(result) == 11)

