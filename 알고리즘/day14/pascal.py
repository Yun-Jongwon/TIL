T=int(input())
for t in range(T):
    num=int(input())
    pascal1=[1]
    pascal2=[1,1]
    print('#{} '.format(t+1))
    if num==1:
        print(1)
        continue
    if num==2:
        print(1)
        print('1 1')
        continue
    print(1)
    print('1 1')

    for n in range(3,num+1):
        if n==3:
            pascal=pascal2
        new_pascal=[1]
        for i in range(len(pascal)-1):
            new_pascal.append(pascal[i]+pascal[i+1])
        new_pascal.append(1)
        pascal=new_pascal
        for i in pascal:
            print(i,end=' ')
        print()





