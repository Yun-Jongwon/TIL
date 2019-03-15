def mine(a,b):
    global result
    if b==0:
        result=a
        return 
    re=a%b
    mine(b,re)



a,b=map(int,input().split())
result=0
i=a
n=b
for n in range(a,b+1):
    i=a
    while i*i<=n:
        if n%i==0:
