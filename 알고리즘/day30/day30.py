def ispossible(x):
    if x==0:
        return 0 if 0 in error_button else 1
    exp=x
    while exp!=0:
        namuzi=exp%10
        if namuzi in error_button:
            return False
        exp=exp//10
    return len(str(x))
target=int(input())
error_button_count=int(input())
error_button=list(map(int,input().split()))

ans=abs(target-100)
for i in range(1000001):
    a= ispossible(i)
    if a!= False:
        ans=min(ans,a+abs(target-i))
print(ans)






