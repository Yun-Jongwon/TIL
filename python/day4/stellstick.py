T=int(input())
for t in range(T):
    num=int(input())

    data=list(map(int,input().split()))
    tuple_data=[]
    for i in range(len(data)//2):
        tuple_data.append([data[2*i],data[2*i+1]])


    for i in range(len(tuple_data)):
        result = tuple_data[i]
        while True:
            first=len(result)
            for j in range(len(tuple_data)):
                if result[len(result)-1]==tuple_data[j][0]:
                    result+=tuple_data[j]
                    break
            if len(result)==first:
                break
        if len(result)==len(tuple_data)*2:
            break
    print(f'#{t+1} ',end="")
    for x in result:
        print(f'{x} ',end="")
    print()





