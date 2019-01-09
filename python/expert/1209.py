for i in range(10):
    x=input()
    box=[]
    set1=set()
    for i in range(100):
        line=list(map(int,input().split()))
        box.append(line)



    rl=0
    lr=0
    for i in range(100):

        set1.add(sum(box[i][:]))
    
        rl=rl+box[i][i]
        lr=lr+box[i][99-i]
    set1.add(rl)
    set1.add(lr)

    for i in range(100):
        down=0
        for j in range(100):
            down=down+box[j][i]
        set1.add(down)

    print(f'#{x} {max(set1)}')
    

