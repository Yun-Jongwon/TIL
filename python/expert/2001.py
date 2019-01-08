num=int(input())
for nnn in range(num):
    box=[]
    N,M =map(int,input().split())
    for i in range (N):
        box.append(list(map(int,input().split())))

    total=0
    for i in range(N-M+1):
        for j in range(N-M+1):
            allsum=0
            for k in range(M):
                allsum=allsum+sum(box[i+k][j:j+M])
            if allsum>total:
                total=allsum

    print(f'#{nnn+1} {total}')
