def multi(x,y):
    if y==1:
        return x*y
    return multi(x,y-1)*x

for i in range(10):
    t=int(input())
    x,y=map(int,input().split())
    print(f'#{i+1} {multi(x,y)}')