for t in range(1):
    num=int(input())
    total_map=[]
    for i in range(100):
        total_map.append(list(map(int,input().split())))
    print(total_map)
    total_map_reverse=list(map(list,zip(*total_map)))
    print(total_map_reverse)
    for i in total_map_reverse:
        if sum(i)<2:
            continue
        for left in range(100):
            if i[left]==2:
                i[left]=0
            if i[left]==1:
                break
        for right in range(-1,-101,-1):
            if i[right]==1:
                i[right]=0
            if i[right]==2:
                break
    while count==0:
        count=0
        for i in total_map_reverse:
            for move in range(len(i)):
                if i[move]==1 and i[move+1]==0:
                    i[move]=0
                    i[move+1]=1

                elif i[move]==2 and i[move-1]==0:
                    i[move]=0
                    i[move-1]=2




