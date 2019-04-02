def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac
def dfs(left,right,cnt,standard):
    global result
    global N
    # global left_standard
    if right>left:
        return
    if cnt==N:
        result+=1
        # print(left,right)
        return
    if left>=standard:

        result+=(2**(N-cnt))*factorial(N-cnt)
        # print(left)
        # print(result)
        # print()
        return
    for i in range(N):

        if visit[i]==0:
            visit[i]=1
            dfs(left+data[i],right,cnt+1,standard-data[i])
            dfs(left,right+data[i],cnt+1,standard)
            visit[i]=0


T=int(input())
for t in range(T):
    N=int(input())
    data=list(map(int,input().split()))

    result=0
    # if sum(data)%2==0:
    #     left_standard = sum(data) // 2
    # else:
    #     left_standard= sum(data) // 2 +1
    standard=sum(data)
    for i in range(N):
        visit = [0] * len(data)
        visit[i]=1
        dfs(data[i],0,1,standard-data[i])

    print("#{} {}".format(t+1,result))