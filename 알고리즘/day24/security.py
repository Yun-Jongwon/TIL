import sys
sys.stdin=open('security','r')
def issafe(y,x):
    global N
    if y>=0 and x>=0 and y<N and x<N:
        return True
    else:
        False


T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    total_map=[]
    for n in range(N):
        data=list(map(int,input().split()))
        total_map.append(data)
    maxcount=0
    for k in range(1,N+2):
        for y in range(N):
            
            for x in range(N):
                count=0

                for smallk in range(y-k+1,y+k):
                    if smallk>=y-k+1 and smallk<=y:
                        for garo in range(smallk-(y-k+1)+1):
                            if garo==0:
                                if issafe(smallk,x-garo) and total_map[smallk][x]==1:
                                    # print(smallk,x-garo)
                                    count+=1
                            else:

                                if issafe(smallk,x-garo) and total_map[smallk][x-garo]==1:
                                    # print(smallk,x-garo)
                                    count+=1
                                if issafe(smallk,x+garo) and total_map[smallk][x+garo]==1:
                                    # print(smallk,x+garo)
                                    count+=1
                    else:
                        for garo in range(y+k-smallk):
                            if garo==0:
                                if issafe(smallk,x-garo) and total_map[smallk][x]==1:
                                    # print(smallk,x-garo)
                                    count+=1
                            else:

                                if issafe(smallk,x-garo) and total_map[smallk][x-garo]==1:
                                    # print(smallk,x-garo)
                                    count+=1
                                if issafe(smallk,x+garo) and total_map[smallk][x+garo]==1:
                                    # print(smallk,x+garo)
                                    count+=1
                                
            # 집 개수 정산
                if count*M-(k*k+(k-1)*(k-1))>=0 and count>maxcount:
                    # print(y,x)
                    # print(count,end=' ')
                    # print(M,end=' ')
                    # print(k)
                    maxcount=count
    print('#{} {}'.format(t+1,maxcount))
        









        