import sys
sys.stdin=open('docking','r')
def dfs(nexttruck,cnt):
    print(nexttruck)
    if nexttruck>=24:
        
        return cnt
    for en in range(len(end_data)):
        if end_data[en]==nexttruck:
            end_data[en]=25
    flag=0
    while flag==0:
        if min(end_data)==25:
            nexttruck=25
            break
        nexttruck_candidate=min(end_data)
        for en in range(len(end_data)):
            # print(end_data)
            if end_data[en]==nexttruck_candidate:
                if start_data[en]>=nexttruck:
                    nexttruck=nexttruck_candidate
                    flag=1
                    break
                else:
                    end_data[en]=25
                    break
    if nexttruck<=24:
        cnt=cnt+1
    return dfs(nexttruck,cnt)
    


T=int(input())
for t in range(T):
    N=int(input())
    start_data=[]
    end_data=[]
    for n in range(N):
        start,end=map(int,input().split())
        start_data.append(start)
        end_data.append(end)
    nexttruck=min(end_data)
    cnt=0
    print('#{} {}'.format(t+1,dfs(nexttruck,cnt)+1))
    

    
