result=[]
n=int(input())
for i in range(8):
    x=list(map(int,input().split()))
    result.append(x)

count=0
for i in result:
    for j in result[i]:
        try:
            if result[i][j:j+n]==result[i][j+n:j]
                count+=1
        except IndexError:
            continue
    col_count=0
    for k in range(8-n):
        if result[i][k] != result[i][n-k-1]:
            break
        col_count+=1
    if col_count==n//2:
        count+=1




