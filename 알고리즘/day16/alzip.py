T=int(input())
for t in range(T):
    N=int(input())
    data=[]
    for n in range(N):
        alphabet,count=input().split()
        for c in range(int(count)):
            data.append(alphabet)
    print('#{}'.format(t+1))
    for i in range(1,len(data)+1):
        if i%10==0:
            print(data[i-1])
        else:
            print(data[i-1],end='')


