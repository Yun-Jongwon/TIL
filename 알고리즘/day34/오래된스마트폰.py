# 5 2 10
# 4 0 5 3 9
# 3 4
# 28




def dfs(present_number,cnt):
    # print(present_number)
    # print("숫자가 {} 일때".format(present_number))
    # print('cnt={}'.format(cnt))
    global target
    global M
    global min_cnt
    if cnt>M:
        return
    if cnt>min_cnt:
        return
    if present_number==target:
        if min_cnt>cnt:
            min_cnt=cnt
        return

    for i in only_can:
        candi=str(i)
        if can_calcul[1]==1:

            if present_number+i<1000:
                if visit[present_number+i] > cnt + len(candi) + 1:
                    visit[present_number+i] = cnt + len(candi) + 1
                    dfs(present_number+i,cnt+len(candi)+1)

        if can_calcul[2]==1:
            if present_number-i>-1:
                if visit[present_number-i] > cnt + len(candi) + 1:
                    visit[present_number-i] = cnt + len(candi) + 1
                    dfs(present_number - i, cnt+len(candi)+1)

        if can_calcul[3]==1:
            if i!=1 and present_number*i<1000:
                if visit[present_number*i] > cnt + len(candi) + 1:
                    visit[present_number*i] = cnt + len(candi) + 1
                    dfs(present_number * i, cnt+len(candi)+1)

        if can_calcul[4]==1:
            if i!=0 :
                if visit[int(present_number / i)] > cnt + len(candi) + 1:
                    visit[int(present_number / i)] = cnt + len(candi) + 1
                    dfs(int(present_number / i), cnt+len(candi)+1)




T=int(input())
for t in range(T):
    N,O,M=map(int,input().split())
    can_number_data=list(map(int,input().split()))
    can_calcul_data=list(map(int,input().split()))# 1-> +, 2-> - , 3->*, 4->/
    can_number=[0]*10
    can_calcul=[0]*5

    for can in can_number_data:
        can_number[can]=1
    for can in can_calcul_data:
        can_calcul[can]=1
    target=int(input())
    visit=[987654321]*1000
    min_cnt=987654321
    only_can = []
    for i in range(0,1000):
        candi=str(i)
        flag=0
        for c in candi:
            if can_number[int(c)]!=1:
                flag=1
                break
        if flag==0:#누를 수 있는 숫자면
            only_can.append(i)
            visit[i] = len(candi)
    for j in only_can:
        dfs(j,len(str(j)))

    if min_cnt==987654321:
        min_cnt=-1
    elif min_cnt!=len(str(target)):
        min_cnt+=1
    print("#%d %d" % (t+1,min_cnt))
