import sys
sys.setrecursionlimit(10**6)


N=int(input())
indata=list(map(int,input().split()))
postdata=list(map(int,input().split()))
ran=1
depth=0


# start=postdata[-1]
# bin=indata.index(start)
#
#
# def binary(podata,idata):
#     if len(podata)==0 or len(idata)==0:
#         return
#     start=podata[-1]
#     print(start,end=' ')
#     bin=idata.index(start)
#     size=len(idata)-1-bin
#     binary(podata[0:-size-1],idata[0:bin])
#     binary(podata[-size-1:-1],idata[bin+1::])
# binary(postdata,indata)

podata=(0,len(postdata)-1)
idata=(0,len(indata)-1)
def binary(podata,idata):
    if idata[0]>idata[1] or podata[0]>podata[1]:
        return
    if idata[0]==idata[1] or podata[0]==podata[1]:
        start = postdata[podata[1]]
        print(start, end=' ')
        return
    start = postdata[podata[1]]
    print(start, end=' ')
    bin=indata.index(start)
    size=idata[1]-bin
    binary((podata[0],podata[1]-size-1),(idata[0],bin-1))
    binary((podata[1]-size,podata[1]-1),(bin+1,idata[1]))




binary(podata,idata)

