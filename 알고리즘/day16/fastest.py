T=int(input())
for t in range(T):
    A,B=input().split()
    B_len=len(B)
    i=0
    count=0
    while i<len(A):
        if A[i]==B[0]:
            if A[i:i+B_len]==B:
                count+=1
                i+=B_len-1
        i+=1
    print('#{} {}'.format(t+1,len(A)-B_len*count+count))

