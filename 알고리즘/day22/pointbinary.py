T=int(input())
for t in range(T):
    data=float(input())
    count=0
    result=''
    while data!=1 and count!=13:
        if data*2>1:
            result+='1'
            data=data*2-1
            count+=1
        elif data*2<1:
            result+='0'
            data=data*2
            count+=1
        elif data*2==1:
            result+='1'
            break
    if count==13:
        result='overflow'
    print('#{} {}'.format(t+1,result))

