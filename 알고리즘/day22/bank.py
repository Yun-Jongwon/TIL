def compare(binary,triple):
    binary_result=0
    triple_result=0
    
    for b in range(len(binary)):
        binary_result+=binary[b]*2**(len(binary)-1-b)
        
    for t in range(len(triple)):
        triple_result+=triple[t]*3**(len(triple)-1-t)
    print(binary_result)
    print(triple_result)
    print()
    if binary_result==triple_result:
        return binary_result



T=int(input())
for tc in range(T):
    binary=input()
    triple=input()
    binary=[int(i) for i in binary]
    triple=[int(i) for i in triple]
    finall=0
    for b in range(len(binary)):
        if binary[b]==0:
            binary[b]=1
        else:
            binary[b]=0
        for t in range(len(triple)):
            finalre=None
            
            if triple[t]==1:
                triple[t]=0
                finalre=compare(binary,triple)
                if finalre !=None:
                    finall=finalre
                    break
                triple[t]=2
                finalre=compare(binary,triple)
                if finalre !=None:
                    finall=finalre
                    break
                triple[t]=1
            elif triple[t]==2:
                triple[t]=0
                finalre=compare(binary,triple)
                if finalre !=None:
                    finall=finalre
                    break
                triple[t]=1
                finalre=compare(binary,triple)
                if finalre !=None:
                    finall=finalre
                    break
                triple[t]=2
            elif triple[t]==0:
                triple[t]=1
                finalre=compare(binary,triple)
                if finalre !=None:
                    finall=finalre
                    break
                triple[t]=2
                finalre=compare(binary,triple)
                if finalre !=None:
                    finall=finalre
                    break
                triple[t]=0
            
        if finall>0:
            break
        if binary[b]==0:
            binary[b]=1
        else:
            binary[b]=0
    print('#{} {}'.format(tc+1,finall))
            