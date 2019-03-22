def player1babygin():
    for i in range(len(player1_data)-2):
        for j in range(i+1,len(player1_data)-1):
            for k in range(j+1,len(player1_data)):
                candi=sorted([player1_data[i],player1_data[j],player1_data[k]])
                
                if (candi[1]-1==candi[0] and candi[1]+1== candi[2]) or (candi[0]==candi[1] and candi[1]==candi[2]):
                    # print(candi)
                    return 1
    return 0
def player2babygin():
    for i in range(len(player2_data)-2):
        for j in range(i+1,len(player2_data)-1):
            for k in range(j+1,len(player2_data)):
                candi=sorted([player2_data[i],player2_data[j],player2_data[k]])
                if (candi[1]-1==candi[0] and candi[1]+1== candi[2]) or (candi[0]==candi[1] and candi[1]==candi[2]):
                    return 2
    return 0


T=int(input())
for t in range(T):
    data=list(map(int,input().split()))
    player1_data=[]
    player2_data=[]
    player1=0
    player2=0
    result=0
    for d in range(len(data)):
        if d%2==0:
            player1_data.append(data[d])
            # print(player1_data)
        else:
            player2_data.append(data[d])
            # print(player2_data)
        if d>=4:
            if len(player2_data)>=3:
                player1=player1babygin()
                player2=player2babygin()
            else:
                player1babygin()
        if player1==1 and (player2==0 or player2==2):
            result=1
            break
        elif player1==0 and player2==2:
            result=2
            break
    print('#{} {}'.format(t+1,result))
        



            

