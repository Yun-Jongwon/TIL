T=int(input())
for t in range(T):
    N=int(input())
    box=[]
    for i in range(N):
        x=input()
        y=" ".join(x)
        box.append(list(map(int,y.split())))
    result=sum(box[int((N-1)/2)][:])
    for i in range(1,int((N+1)/2)):
        result=result+sum( box[int((N-1)/2)+i][i:N-i]) 
        result=result+sum( box[int((N-1)/2)-i][i:N-i])
    print(f'#{t+1} {result}')