import sys
sys.setrecursionlimit(10**9)


N=int(sys.stdin.readline())
indata=list(map(int,sys.stdin.readline().split()))
postdata=list(map(int,sys.stdin.readline().split()))




podata=(0,len(postdata)-1)
idata=(0,len(indata)-1)
result=[0]*N
index=0
inorder_index=[0]*(N+1)
for ii in range(len(indata)):
    inorder_index[indata[ii]]=ii
def binary(podata,idata):
    global index
    if idata[0]>idata[1] or podata[0]>podata[1]:
        return
    if idata[0]==idata[1] or podata[0]==podata[1]:
        start = postdata[podata[1]]
        result[index]=start
        index+=1
        return
    start = postdata[podata[1]]
    result[index] = start
    index += 1
    bin=inorder_index[start]
    size=idata[1]-bin

    binary((podata[0],podata[1]-size-1),(idata[0],bin-1))
    binary((podata[1]-size,podata[1]-1),(bin+1,idata[1]))



binary(podata,idata)
print(' '.join(map(str,result)))

