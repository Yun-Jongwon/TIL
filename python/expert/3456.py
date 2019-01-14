for i in range(int(input())):
    x=list(map(int,input().split()))

    if x[0]==x[1]:
        result=x[2]
    elif x[0]==x[2]:
        result=x[1]
    else:
        result =x[0]
    print(f'#{i+1} {result}')

