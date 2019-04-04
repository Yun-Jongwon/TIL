import sys
sys.stdin=open('elec.txt','r')
def dfs(start,count):
    global min_count
    if start>=len(charger):
        if count<min_count:
            min_count=count
        return
    if count>min_count:
        return
    for i in range(start+charger[start],start,-1):
        dfs(i,count+1)


T=int(input())
for t in range(T):
    data=list(map(int,input().split()))
    total_station=data[0]
    charger=data[1:]
    start=0
    count=0
    min_count=987654321
    dfs(start,count)
    print('#{} {}'.format(t+1,min_count-1))








