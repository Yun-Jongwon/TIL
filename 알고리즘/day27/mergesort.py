import sys
sys.stdin=open('merge.txt','r')
def mergesort(data):
    if len(data)==1:
        return data
    middle=len(data)//2
    left=data[0:middle]
    right=data[middle::]
    left=mergesort(left)
    right=mergesort(right)

    return merge(left,right)
def merge(left,right):
    global count
    result=[]
    if left[-1]>right[-1]:
        count+=1
    while 0<len(left) or 0<len(right):
        if len(left)>0 and len(right):
            if left[0]>=right[0]:
                result.append(right.pop(0))
            else:
                result.append(left.pop(0))
        elif len(left)>0:
            result.append(left.pop(0))
        elif len(right)>0:
            result.append(right.pop(0))
    return result

T=int(input())
for t in range(T):
    N=int(input())
    data=list(map(int,input().split()))
    count=0
    result=mergesort(data)
    print('#{}'.format(t+1),end=' ')
    print(result[len(result)//2],end=' ')
    print(count)

