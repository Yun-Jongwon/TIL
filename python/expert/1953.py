T=int(input())
for t in range(T):
    goo=[]
    option=list(map(int,input().split()))
    dy=option[0]
    dx=option[1]
    start=[option[2]+1,option[3]+1]
    time=option[4]
    for i in range(dy):
        row=list(map(int,input().split()))
        row.insert(0,0)
        row.append(0)
        goo.append(row)
    bound=[0]*(dx+2)
    goo.insert(0,bound)
    goo.append(bound)
    
    queue=[]
    queue.append(start)

    right=[1,3,6,7]
    left=[1,3,4,5]
    up=[1,2,5,6]
    down=[1,2,4,7]
    result=[]


    for j in range(time):
        for i in range(len(queue)):
            present=queue.pop(0)
            y=present[0]
            x=present[1]        
            if goo[y][x]==1 :
                if goo[y][x+1] in right:                    
                    queue.append([y,x+1])                   
                if goo[y+1][x] in down:                    
                    queue.append([y+1,x])                   
                if goo[y][x-1] in left :                   
                    queue.append([y,x-1])                               
                if goo[y-1][x] in up :
                    queue.append([y-1,x])          
            if goo[y][x]==2:
                if goo[y+1][x] in down :
                    queue.append([y+1,x])    
                if goo[y-1][x] in up :
                    queue.append([y-1,x])                   
            if goo[y][x]==3:
                if goo[y][x+1] in right:
                    queue.append([y,x+1])
                if goo[y][x-1] in left :
                    queue.append([y,x-1])                               
            if goo[y][x]==4:
                if goo[y][x+1] in right:
                    queue.append([y,x+1])                    
                if goo[y-1][x] in up :
                    queue.append([y-1,x])
            if goo[y][x]==5:
                if goo[y][x+1] in right:
                    queue.append([y,x+1])                    
                if goo[y+1][x] in down :
                    queue.append([y+1,x])                    
            if goo[y][x]==6:
                if goo[y+1][x] in down :
                    queue.append([y+1,x])                    
                if goo[y][x-1] in left :
                    queue.append([y,x-1])                    
            if goo[y][x]==7:
                if goo[y-1][x] in up :
                    queue.append([y-1,x])                    
                if goo[y][x-1] in left :
                    queue.append([y,x-1])
                    

    ######################################
            goo[y][x]=-1
    # final=[]
    # for i in result:
    #     if i not in final:
    #         final.append(i)
    final=0
    for n in goo:
        final+=n.count(-1)

    print(f'#{t+1} {final}')







        

