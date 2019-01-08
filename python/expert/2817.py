from itertools import combinations




T=int(input())
for re in range(T):
    N,k=map(int,input().split())
    li=list(map(int,input().split()))
    count=0
    for i in range(1,N):

        a=list(map(list, combinations(li, i)))
        b=list(combinations(li, i))
        print(a)
        print(b)
'''        for j in a:
            if sum(j)==k:
                count+=1
            
    print(f'#{re+1} {count}')


'''