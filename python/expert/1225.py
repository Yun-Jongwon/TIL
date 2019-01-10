for i in range(10):
    t=int(input())
    case=list(map(int,input().split()))

    while case[-1]>0:
        for i in range(1,6):
            case.append(case.pop(0)-i)
            if case[-1]<=0:
                break
    print(f'#{t} ',end='')
    for i in range(len(case)-1):
        print(case[i],end=' ')
    print('0')
    
    

