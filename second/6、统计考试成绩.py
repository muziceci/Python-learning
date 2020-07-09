# 统计考试成绩
def average_score(lst):
    sum=0
    for k in lst:
        sum+=lst[k]
    return sum/len(lst)

def sort_scores(lst):
    lst1=sorted(lst,key=lst.get)
    lst2=lst1.reverse()
    lst3={}
    for i in lst1:
        lst3[i]=lst[i]
    return lst3
    
def highest_score(lst):
    temp=0
    flag={}
    for k in lst:
        if lst[k]>temp:
            flag=k
            temp=lst[k]
    return flag,lst[flag]        

def lowest_score(lst):
    temp=101
    flag={}
    for k in lst:
        if lst[k]<temp:
            flag=k
            temp=lst[k]
    return flag,lst[flag]  

if __name__=="__main__":
    student={"zhangsan":90,"lisi":78,"wangermazi":38,"goudan":67,"cuihua":96}
    print("所有同学：",student)
    print("平均成绩：",average_score(student))
    print("按成绩降序排列：",sort_scores(student))
    print("分数最高的同学：",highest_score(student))
    print("分数最低的同学：",lowest_score(student))
