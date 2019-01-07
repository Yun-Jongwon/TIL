for j in range(10):
    num=int(input())
    tall= list(map(int,input().split()))
    count=0
    for i in range(num):
        tall[tall.index(max(tall))]=max(tall)-1
        tall[tall.index(min(tall))]=min(tall)+1
    print(f'#{j+1} {max(tall)-min(tall)}') 

