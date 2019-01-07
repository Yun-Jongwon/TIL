
num=int(input())
tall= list(map(int,input().split()))
print(tall)
count=0
for i in range(len(tall)):
    if i==0 or i==1 or i==num-1 or i==num-2:
        continue
    if tall[i]-tall[i-1]>=2 and tall[i]-tall[i-2]>=2 and tall[i]-tall[i+1]>=2 and tall[i]-tall[i+2]:
        leftright=[tall[i]-tall[i-1],tall[i]-tall[i-2], tall[i]-tall[i+1], tall[i]-tall[i+2]]
        count+=min(leftright)
print(count)
        
 




