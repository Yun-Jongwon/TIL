# nn = 5
# rr = 3
# IsUsed= [0]*(rr+1)
# def GetSome(n , r):
#     for i in range(1, rr+1):
#         print(IsUsed[i], end=' ')
    
#     GetSome


# GetSome(1,1)


cnt = 0
def combination( r , i , d):

    global data, cnt ,n
    if r == 0:
        print(d)
        cnt+=1
        return
    if i==n: return

    combination( r-1, i, d+[data[i]])
    combination( r, i+1, d)

data = [1,2,3,4,5]
n=len(data)
combination( 3, 0, [])
print(cnt)



