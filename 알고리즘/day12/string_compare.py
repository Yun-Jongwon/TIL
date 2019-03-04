T=int(input())
for t in range(T):
    str1=input()
    str2=input()
    pi=[-1,0]
    i=0
    j=1
    while j!=len(str1):
        if str1[i]!=str1[j]:
            if str1[0]==str1[j]:
                pi.append(1)
            else :
                pi.append(0)
            j+=1
        elif str1[i]==str1[j]:
            pi.append(pi[j]+1)
            i+=1
            j+=1
    k=0
    p=0
    result=0
    x=0
    while p!=len(str2):
        if str1[x]==str2[p]:
            p+=1
            x+=1
        else:
            k=k-pi[k]
            p=p+k
            x=0
        if x==len(str1):
            result=1
            break
    print(f'#{t+1} {result}')



