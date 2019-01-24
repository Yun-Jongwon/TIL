a=[[0,1,1,0],[1,2,0,1],[1,0,0,1],[3,1,1,0]]

for i in range(len(a)):
    if 2 in a[i]:
        index=a[i].index(2)
        print(f'{index} {i}')