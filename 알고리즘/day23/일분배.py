T=int(input())
for t in range(T):
    for_range=int(input())
    result=[1]*for_range
    max_percent=0
    visit=[0]*for_range
    def backtrack(depth,percent):
        global max_percent
        global for_range
        
        if percent<max_percent:
            return
        if depth==for_range:
            if percent>max_percent:
                max_percent=percent   
            return
        for i in range(for_range):
            if visit[i]==0:
                if total_data[depth][i]==0:
                    continue
                else:
                    visit[i]=1
                    result[depth]=total_data[depth][i]
                    backtrack(depth+1,percent*(total_data[depth][i]*0.01))
                    visit[i]=0
    total_data=[]
    for i in range(for_range):
        data=list(map(int,input().split()))
        total_data.append(data)
    backtrack(0,1)
    print('#%d %0.6f'%(t+1,max_percent*100))
    
    
        



