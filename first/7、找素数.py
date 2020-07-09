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
    for i in range(2,100):
        if find_prime(i):
            # 输出不换行
            print(i,end=" ")





