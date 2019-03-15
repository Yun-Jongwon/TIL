



a,b=map(int,input().split())
if a==1:
    a=2
for plus in range(a,b+1):
    i=2
    flag=0
    while i*i<=plus:
        if plus%i==0:
            flag=1
            break
        i+=1
    
    if flag==0:
        print(plus)
