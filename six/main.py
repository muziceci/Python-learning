
import os
import sys
import joseph as J

TXT_FILE = "people.txt"
CSV_FILE = "people.csv"
ZIP_FILE = "people.zip"

def creat_joseph(file):
    if file.endswith('.txt'):
        joseph.created_from_txt(file)
    elif file.endswith('.csv'):
        joseph.created_from_csv(file)
    elif file.endswith('.zip'):
        joseph.created_from_zip(file)
    elif os.access(file, os.F_OK):
        print("File is not found")
    else:
        print("输入的不是正确的文件名格式！")
        sys.exit(0)

if __name__ == "__main__":
    joseph = J.Joseph(2, 2)
    # creat_joseph(TXT_FILE)
    # creat_joseph(CSV_FILE)
    # creat_joseph(ZIP_FILE)
    # IN_FILE = str(input("请输入文件名："))# C:/Users/Administrator/Desktop/people.txt
    # creat_joseph(IN_FILE)
    print("被杀掉的依次是：")
    for i in joseph:
        print(i)
    try:
        result = joseph.get_survive_person()
        print("最后留下的人：", result)
    except ValueError as v_e:
        print(v_e)
