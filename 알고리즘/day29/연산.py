
import collections


T=int(input())
for t in range(T):
    start,end=map(int,input().split())
    result_count=987654321
    visit = [0] * 1000000

    queue=collections.deque([(start,0)])
    while queue!=[]:
        print(queue)
        pp=queue.popleft()


        if pp[0]<=0:
            continue
        if pp[0]>1000000:
            continue
        if pp[0]==end:
            result_count=pp[1]
            break
        if visit[pp[0]]==1:
            continue
        visit[pp[0]] = 1
        next1=(pp[0]*2,pp[1]+1)
        print(next1)

        next2=(pp[0]+1,pp[1]+1)

        next3=(pp[0]-1,pp[1]+1)

        next4=(pp[0]-10,pp[1]+1)


        queue.append(next1)
        queue.append(next2)

        queue.append(next3)

        queue.append(next4)
    print('#{} {}'.format(t + 1, result_count))


