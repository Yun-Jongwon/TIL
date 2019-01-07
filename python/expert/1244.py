#for j in range(10):
money=[]
tall= str(input())
num=int(input())
count=0
for i in range(num):
    for j in range(len(tall)):
        for k in range(i+1,len(tall)):
            twin=tall
            temp=twin[j]
            twin.replace(twin[k],twin[j])
            twin.replace(twin[k],temp)
            if int(tall) <int(twin):
                tall=twin
    print(tall)
    


    if i+1==num:
        break

print(money)

            


