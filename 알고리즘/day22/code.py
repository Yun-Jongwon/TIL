import sys
sys.stdin=open('이진수','r')

T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    total_map=[]
    A,B,C,D,E,F=10,11,12,13,14,15
    password=[[2,1,1],[2,2,1],[1,2,2],[4,1,1],[1,3,2],[2,3,1],[1,1,4],[3,1,2],[2,1,3],[1,1,2]]
    for n in range(N):
        data=input()
        total_map.append(data)### input받기


    for i in range(len(total_map)):
        new_string=''
        for j in range(len(total_map[i])):
            if total_map[i][j]=='0':
                new_string+='0000'
            elif total_map[i][j]=='1':
                new_string+='0001'
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

                for g in range(3):
                    result=new_i%2
                    new_data.append(result)
                    new_i=new_i//2
                new_data.append(new_i)
                new_data=list(reversed(new_data))
                # print(new_data)
               

                
                result_string=''
                for k in new_data:
                    strr=str(k)
                    result_string+=strr
                new_string+=result_string
        total_map[i]=new_string# 2진법으로 변환
    # print(total_map)
    result_print=[]
    for i in range(len(total_map)):
        first_one_count=0
        first_zero_count=0
        second_one_count=0
        eight_password=[]
        eight_password_weight=[]
        for j in range(-1,-len(total_map[i])-1,-1):
            # if not (second_one_count==0 and first_zero_count==0 and first_one_count==0):
                # print(second_one_count,first_zero_count,first_one_count)
            if len(eight_password)==8:
                # print(eight_password)
                if ((eight_password[1]+eight_password[3]+eight_password[5]+eight_password[7])*3+eight_password[0]+eight_password[2]+eight_password[4]+eight_password[6])%10==0:

                    # print(sum(eight_password))
                    if not eight_password in result_print:
                        result_print.append(eight_password)
                    
                    first_one_count=0
                    first_zero_count=0
                    second_one_count=0
                    eight_password=[]
                else:
                    first_one_count=0
                    first_zero_count=0
                    second_one_count=0
                    eight_password=[]

            if second_one_count>0 and total_map[i][j]=='0':
                standard=min(first_one_count,first_zero_count,second_one_count)

                standard_list=[second_one_count//standard,first_zero_count//standard,first_one_count//standard]
                for p in range(len(password)):
                    if password[p]==standard_list:
                        eight_password.append(p)
                        # print(eight_password)
                        break
                # eight_password_weight.append(standard)
                first_one_count=0
                first_zero_count=0
                second_one_count=0
            elif first_zero_count>0 and total_map[i][j]=='1':
                second_one_count+=1
            elif first_one_count>0 and total_map[i][j]=='0':
                first_zero_count+=1         
            elif total_map[i][j]=='1':#처음 1을 발견
                first_one_count+=1
    total_print=0
    for total in result_print:
        total_print+=sum(total)

    print('#{} {}'.format(t+1,total_print))




                    



    # print(total_map)

