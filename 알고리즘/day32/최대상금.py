# 10
#1 123 1
#2 2737 1
#3 757148 1
#4 78466 2
#5 32888 2
#6 777770 5
#7 436659 2
#8 431159 7
#9 112233 3
# 456789 10
def dfs(data,p_cnt):
    global cnt
    if p_cnt==cnt:
        result.append(int(data))
        return
    money = []
    for d in data:
        money.append(d)
    next_data_list=set()
    for i in range(len(money)-1):
        for j in range(i+1,len(money)):
            money[i],money[j]=money[j],money[i]
            next_data=''.join(money)
            next_data_list.add(next_data)
            money[i], money[j] = money[j], money[i]
    for ne in next_data_list:
        dfs(ne,p_cnt+1)


T=int(input())
for t in range(T):
    data,incnt=input().split()
    cnt=int(incnt)
    if cnt>5:
        cnt=5
    result=[]
    dfs(data,0)
    if int(incnt)>5 and int(incnt)%2==0:
        cnt=1
        a=str(max(result))
        result=[]
        dfs(a,0)

    print("#{} {}".format(t+1,max(result)))
