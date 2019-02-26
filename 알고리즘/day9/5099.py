T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    data=list(map(int,input().split()))
    exist=[]
    for m in range(1,M+1):
        exist.append(m)
    hwaduck=[]
    hwaduck_exist=[]
    for n in range(N):
        hwaduck.append(data.pop(0))
        hwaduck_exist.append(exist.pop(0))
    while len(hwaduck)!=1:
        if len(hwaduck)<N and data!=[]:
            hwaduck.append(data.pop(0))
            hwaduck_exist.append(exist.pop(0))
        output_cheeze=hwaduck.pop(0)
        output_exist=hwaduck_exist.pop(0)
        output_cheeze=output_cheeze//2
        if output_cheeze!=0:
            hwaduck.append(output_cheeze)
            hwaduck_exist.append(output_exist)
    print(f'#{t+1} {hwaduck_exist[0]}')
