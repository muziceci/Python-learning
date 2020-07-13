# 约瑟夫环,加上人的属性,人的属性是从txt文件读出的
        
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
result = get_survive_number(total_number,kill_number)
assert(result == 4) #如果预期结果不是4则程序中断，报错

people=open("E:/git/Python-learning/third/people.txt")
people_lst=[i[:-1].split(',') for i in people.readlines()]
    
print("最后留下的人的属性:",end=" ")
print("姓名:",people_lst[result-1][0]," 年龄:",people_lst[result-1][1]," 性别:",people_lst[result-1][2])
print("被杀掉的编号:",kill_lst)