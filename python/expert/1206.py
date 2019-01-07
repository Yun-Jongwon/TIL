for j in range(10):
    num=int(input())
    tall= list(map(int,input().split()))
    count=0
    for i in range(len(tall)):
        if i==0 or i==1 or i==len(tall)-1 or i==len(tall)-2:
            continue
        if tall[i]-tall[i-1]>=1 and tall[i]-tall[i-2]>=1 and tall[i]-tall[i+1]>=1 and tall[i]-tall[i+2]>=1:
            leftright=[tall[i]-tall[i-1] , tall[i]-tall[i-2] ,  tall[i]-tall[i+1] ,  tall[i]-tall[i+2]]
            count+=min(leftright)
    print(f'#{j+1} {count}')
        