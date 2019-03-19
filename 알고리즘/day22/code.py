T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    total_map=[]
    A,B,C,D,E,F=10,11,12,13,14,15
    for n in range(N):
        data=input()
        total_map.append(data)
    for i in range(len(total_map)):
        new_string=''
        for j in range(len(total_map[i])):
            if total_map[i][j]=='0':
                new_string+='0'
            elif total_map[i][j]=='1':
                new_string+='1'
            else:
                new_data=[]
                if total_map[i][j]=='A':
                    new_i=A
                elif total_map[i][j]=='B':
                    new_i=B
                elif total_map[i][j]=='C':
                    new_i=C
                elif total_map[i][j]=='D':
                    new_i=D
                elif total_map[i][j]=='E':
                    new_i=E
                elif total_map[i][j]=='F':
                    new_i=F
                else:new_i=int(total_map[i][j])

                for g in range(3,-1,-1):
                    result=(new_i&(1<<g))>>g
                    new_data.append(result)
                result_string=''
                for k in new_data:
                    strr=str(k)
                    result_string+=strr
                new_string+=result_string
        total_map[i]=new_string
        for i in range(len(total_map)):
            first_one_count=0
            first_zero_count=0
            second_one_count=0
            for j in range(-1,-len(total_map[i])-1,-1):
                if total_map[i][j]=='1':
                    first_one_count+=1
                elif first_one_count>0 and total_map[i][j]=='0':
                    first_zero_count+=1
                elif first_zero_count>0 and total_map[i][j]=='1':
                    second_one_count+=1
                elif second_one_count>0 and total_map[i][j]=='0':
                    standard=min(first_one_count,first_zero_count,second_one_count)
                    standard_list=[second_one_count//,first_zero_count,first_one_count]

                    
                    standard*56



    # print(total_map)


password=[[2,1,1],[2,2,1],[1,2,2],[4,1,1],[1,3,2],[2,3,1],[1,1,4],[3,1,2],[2,1,3],[1,1,2]]
