import sys
sys.stdin=open('binary.txt','r')
def binary(data):
    global want
    global resultright,resultleft,result
    if data==[]:
        return
    if len(data)==1:
        if data[0]==want:
            result+=1
            return
        else:
            return
    if len(data)%2==0:
        middle=(len(data)-1)//2
    else:
        middle=len(data)//2
    # print(want)
    if data[middle]==want:
        # print(want)
        result+=1
        return
    # print(data[middle])
    if data[middle]<want:
        if resultleft==1 and resultright==0:
            resultleft=0
            resultright=1
            return binary(data[middle+1::])
        elif resultleft==0 and resultright==0:
            resultright=1
            return binary(data[middle+1::])
        else:
            return
    elif data[middle]>want:
        if resultleft==0 and resultright==1:
            resultright=0
            resultleft=1
            return binary(data[0:middle])
        elif resultleft==0 and resultright==0:
            resultleft=1
            return binary(data[0:middle])
        else:
            return
T=int(input())
for t in range(T):
    num1,num2=input().split()
    A=sorted(list(map(int,input().split())))
    B=list(map(int,input().split()))
    result=0
    for b in B:
        resultright = 0
        resultleft = 0
        want=b
        binary(A)
    print('#{} {}'.format(t+1,result))
