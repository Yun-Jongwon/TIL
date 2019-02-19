
def bomb(bom_map,H,W,N):
    stack=[]
    last_N=N-1
    dy=[0,1,0,-1]
    dx=[1,0,-1,0]
    result=[]
    for w in range(W):
        for h in range(H):
            if bom_map[h][w] != 0:
                stack.append((h,w))
                break
        while stack !=[]:
            y,x=stack.pop()
            if bom_map[y][x] > 1:
                for alpha in range(1,bom_map[y][x]):
                    for dir in range(4):
                        if Issafe(y+dy[dir]*alpha,x+dx[dir]*alpha,H,W) and bom_map[y+dy[dir]*alpha][x+dx[dir]*alpha]>1:
                            stack.append((y+dy[dir]*alpha,x+dx[dir]*alpha))
                        else :
                            bom_map[y+dy[dir]*alpha][x+dx[dir]*alpha]=0

                bom_map[y][x]=0
            elif bom_map[y][x] == 1:
                bom_map[y][x]=0
        

        ###밑으로내리기
        for result_x in range(W):
            temp=[]
            for result_y in range(-1,-H-1,-1):                
                if bom_map[result_y][result_x] !=0:
                    temp.append(bom_map[result_y][result_x])
            for y in range(-1,-H-1,-1):
                if temp!=[]:
                    bom_map[y][result_x] = temp.pop(0)
                else:
                    bom_map[y][result_x] = 0



        if last_N!=0:
            bomb(bom_map,H,W,N-1)
        else:
            total_sum=0
            for i in bom_map:
                total_sum+=sum(i)
            result.append(total_sum)
    return min(result)
            
        





def Issafe(y,x,h,w):
    if y>=0 and x>=0 and y<h and x<w:
        return True



T=int(input())
for t in range(T):
    N,W,H=map(int,input().split())
    total_map=[]
    for h in range(H):
        w=list(map(int,input().split()))
        total_map.append(w)
    result=[]
    final=bomb(total_map,H,W,N)
    print(final)
    
