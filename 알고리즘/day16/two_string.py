T=int(input())
for t in range(T):
    num1,num2=map(int,input().split())
    data1=list(map(int,input().split()))
    data2=list(map(int,input().split()))
    if len(data1)>len(data2):
        short_data=data2
        long_data=data1
    else:
        short_data=data1
        long_data=data2
    sum=-500
    for i in range(len(long_data)-len(short_data)+1):
        new_sum=0
        for j in range(len(short_data)):
            new_sum+=short_data[j]*long_data[j+i]
        if new_sum>sum:
            sum=new_sum
    print(sum)

