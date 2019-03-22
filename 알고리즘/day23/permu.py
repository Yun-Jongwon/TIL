#4중복P3
visit=[0]*5
result=[0]*3
def backtrack(spot):
    if spot==3:
        print(result)
        return
    for i in range(1,5):
        result[spot]=i
        # visit[i]=1
        backtrack(spot+1)
        # visit[i]=0
backtrack(0)


#4P3
visit=[0]*5
result=[0]*3
def backtrack2(spot):
    if spot==3:
        print(result)
        return
    for i in range(1,5):
        if visit[i]==0:
            result[spot]=i
            visit[i]=1
            backtrack2(spot+1)
            visit[i]=0
backtrack2(0)
    
