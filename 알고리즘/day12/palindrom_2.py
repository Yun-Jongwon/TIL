
for t in range(10):
    num=input()
    total_map=[]
    for n in range(100):
        garo=" ".join(input())
        total_map.append(list(garo.split()))
    result=1



    for i in total_map:
        for k in range(1,100):
            for x in range(100-k):
                one=i[x:x+k+1]
                two=list(reversed(one))
                if one==two:
                    if len(one)>result:
                        result=len(one)




    total_map_revers=list(map(list,zip(*total_map)))


    for i in total_map_revers:
        for k in range(1,100):
            for x in range(100-k):
                one=i[x:x+k+1]
                two=list(reversed(one))
                if one==two:
                    if len(one)>result:
                        result=len(one)



    print(f'#{t+1} {result}')


