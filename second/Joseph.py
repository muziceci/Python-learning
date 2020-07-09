# 初始化所有人编号为列表lst
# 判断lst长度，如果为1，就输出编号lst[0]
# 第一个kill_number之前的数存进一个列表font_lst,之后的数存进back_lst
# 去除kill_number,将font_lst追加到back_lst,循环

number1=int(input("请输入总人数:"))
number2=int(input("请输入会被杀掉的报数:"))
lsta=[]
for i in range(number1):
    lsta.append(i+1) 

def solve_joseph(total_number,kill_number,lst):   
    if total_number==1:
        # return lst[0]
        print(lst[0])
    else:         
        font_lst=lst[0:kill_number-1]  #包括0不包括kill_number
        back_lst=lst[kill_number:total_number]
        back_lst.extend(font_lst)    #形成新列表back_lst
        solve_joseph(len(back_lst),kill_number,back_lst)

print("最后留下的人的编号:",end=" ")
solve_joseph(number1,number2,lsta)


