data=[56,3,4,8,65,8,95,3,4545,68,5]
def select(start,end):
    if start==end:
        return
    standard=min(data[start:end])
    for i in range(start,end):
        if data[i]==standard:
            data[start],data[i]=data[i],data[start]
            break
    select(start+1,end)

select(0,len(data))
print(data)
            

        




