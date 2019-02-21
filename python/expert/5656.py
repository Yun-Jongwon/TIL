import copy
import math

result = []
dy=[0,1,0,-1]
dx=[1,0,-1,0]
def bomb(bom_map,H,W,N):
    stack=[]
    last_N=N-1
    for w in range(W):
        soon_bom = copy.deepcopy(bom_map)
        for h in range(H):
            if soon_bom[h][w] != 0:
                stack.append((h,w))
                break
        while stack !=[]:
            y,x=stack.pop()
            if soon_bom[y][x] > 1:
                for alpha in range(1,soon_bom[y][x]):
                    for dir in range(4):
                        if Issafe(y+dy[dir]*alpha,x+dx[dir]*alpha,H,W):
                            if soon_bom[y+dy[dir]*alpha][x+dx[dir]*alpha]>1:
                                stack.append((y+dy[dir]*alpha,x+dx[dir]*alpha))
                            elif soon_bom[y+dy[dir]*alpha][x+dx[dir]*alpha]==1:
                                # print(y+dy[dir]*alpha,x+dx[dir]*alpha)
                                soon_bom[y+dy[dir]*alpha][x+dx[dir]*alpha]=0

                soon_bom[y][x]=0
            elif soon_bom[y][x] == 1:
                soon_bom[y][x]=0
        

        ###밑으로내리기
        for result_x in range(W):
            temp=[]
            for result_y in range(-1,-H-1,-1):                
                if soon_bom[result_y][result_x] !=0:
                    temp.append(soon_bom[result_y][result_x])
            for y in range(-1,-H-1,-1):
                if temp!=[]:
                    soon_bom[y][result_x] = temp.pop(0)
                else:
                    soon_bom[y][result_x] = 0



        if last_N!=0:
            bomb(soon_bom,H,W,N-1)
        else:
            total_sum=0
            for i in soon_bom:
                for j in range(W):
                    if i[j]!=0:
                        total_sum+=1
            result.append(total_sum)
        return


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
    bomb(total_map,H,W,N)
    print(min(result))
    
