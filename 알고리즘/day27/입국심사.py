N,M=map(int,input().split())
min_time=987654321
total_data=[]
for n in range(N):
    data=int(input())
    if data<min_time:
        min_time=data
    total_data.append(data)
binary_from=0
binary_to=min_time*M
while (binary_from!=binary_to) and (binary_from+1 != binary_to):
    middle=(binary_from+binary_to)//2
    count=0
    for data in total_data:
        count+=middle//data
    if count<M:
        binary_from=middle
    elif count>=M:
        binary_to=middle
print(binary_to)



28

7
10
29
28



