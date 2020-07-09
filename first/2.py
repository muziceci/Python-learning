import random
a=[]
for i in range(40):
    a.append(random.randint(1,100))

sum=0
for i in a:
    sum=sum+i

average=sum/len(a)
print("平均成绩：",average)

temp=0
for i in a:
    if(i<average):
        temp+=1
print("小于平均成绩的学生人数：",temp)
a.sort()
# print(a)
a.reverse()
print("列表的升序排列结果：",a)
