T=int(input())
for t in range(T):
    num=int(input())
    data=list(map(int,input().split()))
    sort_data=sorted(data)
    result=[]
    for i in range(len(sort_data)//2):
        result.append(sort_data[len(sort_data) - 1 - i])
        result.append(sort_data[i])

    print(f'#{t+1} ',end="")
    for i in result:
        print(i,end=" ")
    print()