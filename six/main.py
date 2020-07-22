
import joseph as J
import reader

TXT_FILE = "file/people.txt"
CSV_FILE = "file/people.csv"
ZIP_FILE = "file/people.zip"
ERROR_FILE = "pe.txt"


if __name__ == "__main__":
    people_lst = reader.get_people_lst_from(CSV_FILE)
    # people_lst = reader.get_people_lst_from(ERROR_FILE)
    joseph = J.Joseph(2, 3)
    joseph.append(people_lst)
    print("被杀掉的依次是：")
    for i in joseph:
        print(i)
    try:
        result = joseph.get_survive_person()
        print("最后留下的人：", result)
    except ValueError as v_e:
        print(v_e)
