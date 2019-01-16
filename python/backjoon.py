T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    n=b-a
    x=int(n**(1/2))
    
    if x**2+x<n:
        print(2*x+1)
    elif x**2<n:
        print(2*x)
    else:        
        print(2*x-1)