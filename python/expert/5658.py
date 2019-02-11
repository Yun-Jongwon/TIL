T=int(input())
for o in range(T):
    sx,sy =input().split()
    N=int(sx)
    K=int(sy)
    full_number=input()
    full_number_list=[i for i in full_number]
    inline=N//4
    result=set()
    one=''
    for j in range(inline):
        for i in range(len(full_number)):
            one+=full_number_list[i]
            if (i+1)%inline==0:
                result.add(one)
                one=''
        temp=full_number_list.pop()
        full_number_list.insert(0,temp)
    hexa='0x'
    result_list=list(result)
    ten=[]
    for k in result_list:
        x=hexa+k
        ten.append(int(x,16))
    sort_ten=list(reversed(sorted(ten)))

    print(f'#{o+1} {sort_ten[K-1]}')


