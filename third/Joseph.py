# 约瑟夫环,加上人的属性
class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def Print(self):
        print("姓名：%s,年龄：%s,性别：%s"%(self.name,self.sex,self.name))

kill_lst = []
 
def get_survive_number(number,step):
    joseph_lst = [i for i in range(1,total_number+1)]
    print("约瑟夫环编号是：",joseph_lst)
    temp = 1  #计数
    index = 0 #元素下标
    while len(joseph_lst)>1:
        if temp == step:
            kill_lst.append(joseph_lst[index])
            joseph_lst.pop(index)
            temp = 1
        else:
            temp += 1
            index += 1
        if index == number-len(kill_lst):
            index = 0
    return joseph_lst[0]

total_number = int(input("请输入总人数:"))
kill_number = int(input("请输入会被杀掉的报数:"))

p1 = Person('Jack',19,'male')
p2 = Person('Vivi',17,'female')
p3 = Person('Mark',21,'male')
person_lst = [p1,p2,p3]
result = get_survive_number(total_number,kill_number)
assert(result == 3) #如果预期结果不是3则程序中断，报错
print("最后留下的人的属性:",end=" ")
person_lst[result-1].Print()
print("被杀掉的编号:",kill_lst)