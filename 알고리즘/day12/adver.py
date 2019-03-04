num=input()
str1=input()
pi=[-1,0]
i=0
j=1
while j!=len(str1):
    if str1[i]!=str1[j]:
        if str1[0]==str1[j]:
            pi.append(1)
        else :
            pi.append(0)
            i=0
        j+=1
    elif str1[i]==str1[j]:
        pi.append(pi[j]+1)
        i+=1
        j+=1
for i in range(-1,-len(pi)-1,-1):
    if pi[-1]==0:
        result=len(str1)
        break
    if pi[i]==1 :
        result=len(pi[0:i-1])
        break
print(pi)
print(result)







#[-1, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 4개반복 16개 ,0이 4개
#
