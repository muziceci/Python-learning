import random

scores=[]
for i in range(40):
    scores.append(random.randint(1,100))

def get_average_scores(lst):
    sum=0
    for i in lst:
        sum=sum+i
    return sum/len(scores)

def filter_under_average(lst):
    count_scores=0
    for i in lst:
        if(i<get_average_scores(lst)):
            count_scores+=1   
    return count_scores

sorted_scores=sorted(scores,reverse=True)

print("平均成绩：",get_average_scores(scores))
print("小于平均成绩的学生人数：",filter_under_average(scores))
print("列表的降序排列结果：",sorted_scores)
