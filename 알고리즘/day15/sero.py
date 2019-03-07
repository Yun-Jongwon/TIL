T=int(input())
for t in range(T):
    total_data=[]
    for i in range(5):
        data=' '.join(input()).split()
        total_data.append(data)
    max_len=0
    for j in total_data:
        if len(j)>max_len:
            max_len=len(j)
    result_string=''
    for x in range(max_len):
        for y in range(5):
            if total_data[y]!=[]:
                result_string+=total_data[y].pop(0)
    print(result_string)
