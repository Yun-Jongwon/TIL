for a in range(int(input())):
    x=input()

    other=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    tc=list(input().split())
    result=[]
    for i in other:
        for j in range(tc.count(i)):
            result.append(i)
    print (f'#{a+1} {" ".join(result)}')