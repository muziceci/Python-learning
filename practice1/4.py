a={}
a[0]=0
a[1]=1
for i in range(2,101):
    a[i]=a[i-1]+a[i-2]
  
print(a[100])

