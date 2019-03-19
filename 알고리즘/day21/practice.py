data=list(map(int,input().split()))
result=0
# for i in range(0,7):
#     result+=data[i]*2**(7-i-1)
# print(result,end=', ')
# result=0
# for i in range(7,14):
#     result+=data[i]*2**(14-i-1)
# print(result)
i=0
j=0
count=0
while count!=len(data):
    if i==7:
        i=0
    result+=data[count]*2**(7-i-1)
    if i==6:
        print(result,end=', ')
        
        result=0
    i+=1  
    count+=1



