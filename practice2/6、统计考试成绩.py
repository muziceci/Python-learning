# 统计考试成绩
def ave(stu):
    sum=0
    for k in stu:
        sum+=stu[k]
    return sum/len(stu)

def sort(stu):
    stu1=sorted(stu,key=stu.get)
    stu2=stu1.reverse()
    stu3={}
    for i in stu1:
        stu3[i]=stu[i]
    return stu3
    
def highest(stu):
    temp=0
    flag={}
    for k in stu:
        if stu[k]>temp:
            flag=k
            temp=stu[k]
    return flag,stu[flag]        

def lowest(stu):
    temp=101
    flag={}
    for k in stu:
        if stu[k]<temp:
            flag=k
            temp=stu[k]
    return flag,stu[flag]  

if __name__=="__main__":
    student={"zhangsan":90,"lisi":78,"wangermazi":38,"goudan":67,"cuihua":96}

    print("所有同学：",student)
    print("平均成绩：",ave(student))
    print("按成绩降序排列：",sort(student))
    print("分数最高的同学：",highest(student))
    print("分数最低的同学：",lowest(student))
