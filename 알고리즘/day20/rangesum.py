data=[5,1,-4,2,-1,-5,-2,8,-3,6]
rangesum=[0]*len(data)
rangesum[0]=data[0]

for i in range(1,len(data)):
    # if rangesum[i-1]>0:
    #     rangesum[i]=rangesum[i-1]+data[i]
    # else:
    #     rangesum[i]=data[i]
    rangesum[i]=max(rangesum[i-1]+data[i],data[i])
print(rangesum)
for k in range(len(rangesum)):
    if rangesum[k]==max(rangesum):
        result=k
resultlist=[]
for j in range(result,0,-1):
    if rangesum[j]==data[j]:
        resultlist.append(data[j])
        break
    resultlist.append(data[j])
print(resultlist)
    

