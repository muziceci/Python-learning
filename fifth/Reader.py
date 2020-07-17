import csv
import zipfile


def txt_reader(file):
    with open(file) as people:
        lst = [i.split(',') for i in people]
    return lst

def csv_reader(file):
    lst = []
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        for i in reader:
            lst.append(i)
    # csv_file.close()  
    return lst

def zip_reader(file):
    lst = []
    zip_file = zipfile.ZipFile(file)   #解压zip文件
    content = zip_file.open(zip_file.namelist()[0]).readlines()  #逐行读取txt文件内容
    for i in content:
        lst.append(i.decode('ascii').split(','))#bytes转化为str
    zip_file.close()
    return lst

if __name__ == "__main__":
    txt_lst = txt_reader("people.txt")
    assert(len(txt_lst) == 8)
    print("测试reader")



