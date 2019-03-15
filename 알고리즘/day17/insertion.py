daa=[1,9,3,6,7,0,4,9,5,5]

for j in range(1,len(daa)):
    temp=daa[j]
    i=j-1
    while i>=0 and daa[i]>temp:
        daa[i+1]=daa[i]
        i=i-1
    daa[i+1]=temp
print(daa)
