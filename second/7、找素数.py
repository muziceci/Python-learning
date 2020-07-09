# 找到1-100的素数并输出
def find_prime(n):
    flag=1
    for i in range(2,n):
        if n%i==0:
            flag=0
    if flag==1:
        return True
    else:
        return False

if __name__=="__main__":
    print("1-100的素数有：")
    min_num=2
    max_num=100
    for i in range(min_num,max_num):
        if find_prime(i):            
            print(i,end=" ")# 输出不换行





