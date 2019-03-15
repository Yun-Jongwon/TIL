T=int(input())
for t in range(T):
    n,m=map(int,input().split())
    data=[0]*(n+1)
    for d in range(1,n+1):
        data[d]=d-1
    list_data=list(map(int,input().split()))
    for l in list_data:
        result=data[l]
        for i in range(1,n+1):
            if data[i]<result:
                data[i]+=1
        data[l]=0
        print(result,end=' ')
        
    
    

    
