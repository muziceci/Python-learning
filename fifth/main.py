# import People as P
import Joseph as J

joseph = J.Joseph(2, 1)
# joseph.creat_people_from_txt("people.txt")
# # joseph.creat_people_from_csv("people.csv")
joseph.creat_people_from_zip("people.zip")

print("被杀掉的依次是：")
for i in joseph:
    print(i)
result = joseph.get_survive_person()
print("最后留下的人：", result)
