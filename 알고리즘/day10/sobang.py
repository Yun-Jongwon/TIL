P,F=map(int,input().split())
pump=list(map(int,input().split()))
watercar=list(map(int,input().split()))
total=pump[:]
for i in range(len(watercar)):
    for j in range(len(pump)):
        if watercar[i]<pump[j]:
            pump.insert(j,-watercar[i])
            print(pump)
            break
result=0
for p in range(len(pump)):
    if pump[p]<0:
        
        if p-1>0 and pump[p-1]>0 pump[p+1]<0:






# 좌우가 2개이상씩 있으면 최소값선택택