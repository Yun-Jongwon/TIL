T=int(input())
pattern=['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
for t in range(T):
    data=''
    N,M=map(int,input().split())
    for n in range(N):
        data+=input()
    result=[]
    print(data)
    for i in range(-1,-len(data),-1):
        if data[i]=='1':
            j=0
            point=i
            
            while j!=8:
                for p in range(10):
                    
                    if data[point-6:point+1] == pattern[p]:
                        result.append(p)
                        point-=7
                        j+=1
                        break

            break
    if ((result[1]+result[3]+result[5]+result[7])*3+result[0]+result[2]+result[4]+result[6])%10==0:
        result_print=sum(result)
    else:
        result_print=0
    print('#{} {}'.format(t+1,result_print))
