import People as P
import Joseph as J

joseph = J.Joseph()
joseph.set_step(2)
with open("E:/git/Python-learning/fourth/people.txt") as people:
    lst = [i[:-1].split(',') for i in people]

people_lst = []
for i in lst:
    people_lst.append(P.Person(i[0], int(i[1]), i[2]))

for i in people_lst:
    joseph.append(i)


def test_num(number):
    assert(number == 3)


result = joseph.get_survive_number()
print("最后留下的人：", result)