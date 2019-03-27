import sys
sys.stdin=open('quick.txt','r')
def partition(A,L,r):
    pivot=A[L]
    i=L
    for j in range(L+1,r):
        if pivot>A[j]:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[L],A[i]=A[i],A[L]
    return i


def quicksort(A,L,r):
    if L<r:
        s=partition(A,L,r)
        quicksort(A,L,s)
        quicksort(A,s+1,r)
# A=[11,45,22,81,23,34,99,22,17,8]
T=int(input())
for t in range(T):
    N=input()
    A=list(map(int,input().split()))
    quicksort(A,0,len(A))
    print('#{} {}'.format(t+1,A[len(A)//2]))