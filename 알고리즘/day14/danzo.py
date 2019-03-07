T=int(input())
for t in range(T):
    N=int(input())
    data=list(map(int,input().split()))
    danzo=-1
    for i in range(len(data)-1):
        for j in range(i+1,len(data)):
            result=str(data[i]*data[j])
            flag=0
            for k in range(len(result)-1):
                if int(result[k])>int(result[k+1]):
                    flag=1
                    break
            if flag==0:
                if int(result)>danzo:
                    danzo=int(result)
    print('#{} {}'.format(t+1,danzo))








