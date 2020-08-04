from josephus.use_cases.csv_reader import CsvReader
from josephus.use_cases.txt_reader import TxtReader
from josephus.use_cases.zip_reader import ZipReader


def get_people_lst_from(file: str) -> list:
    lst = []
    if file.endswith('.txt'):
        txt_reader = TxtReader(file)
        lst = txt_reader.reader()
    elif file.endswith('.csv'):
        csv_reader = CsvReader(file)
        lst = csv_reader.reader()
    elif file.endswith('.zip'):
        zip_reader = ZipReader(file)
        lst = zip_reader.reader()
    else:
        raise FileNotFoundError("请输入正确的文件路径！")
    return lst

