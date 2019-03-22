data=[-1,3,-9,6,7,-6,1,5,4,-2]
visit=[0]*len(data)
def backtrack(spot):
    if spot==len(data):
        total_sum=0
        for v in range(len(visit)):
            if visit[v]==1:
                total_sum+=data[v]
        if total_sum==10:
            for v in range(len(visit)):
                if visit[v]==1:
                    print(data[v],end=' ')
            print()

        return
    visit[spot]=1
    backtrack(spot+1)
    visit[spot]=0
    backtrack(spot+1)

backtrack(0)