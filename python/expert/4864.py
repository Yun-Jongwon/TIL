T=int(input())
for t in range(T):
    a=input()
    b=input()
    count=0
    for i in range(len(b)-len(a)+1):
        if b[i:i+len(a)]==a:
            count+=1
    if count!=0:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')