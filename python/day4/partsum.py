T=int(input())
for t in range(T):
    N,K=map(int,input().split())
    count_answer=0
    A=[i for i in range(1,13)]

    for i in range(1<<12):
        part=[]
        for j in range(13):
            if i & (1<<j):
                part.append(A[j])
        if sum(part)==K and len(part)==N:
            count_answer+=1
    print(f'#{t+1} {count_answer}')

