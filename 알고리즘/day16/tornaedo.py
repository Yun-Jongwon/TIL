T=int(input())
for t in range(T):
    N=int(input())
    total_data=[]
    for n in range(N):
        data=list(input().split())
        total_data.append(data)

    one_total_data=list(map(list,zip(*total_data[::-1])))
    two_total_data=list(map(list,zip(*one_total_data[::-1])))
    three_total_data=list(map(list,zip(*two_total_data[::-1])))
    print('#{}'.format(t+1))
    for n in range(N):
        print(*one_total_data[n],sep='',end=' ')
        print(*two_total_data[n], sep='', end=' ')
        print(*three_total_data[n], sep='', end=' ')
        print()
    print(*total_data[::-1])




