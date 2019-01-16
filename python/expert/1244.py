'''
import copy

def changee(tall,count):
    real_tall=copy.deepcopy(tall)
    total=[]
    for i in range(len(tall)):
        for j in range(i+1,len(tall)):
            twin=copy.deepcopy(real_tall)
            twin[i],twin[j]=twin[j],twin[i]
            total.append(twin)
           # if changee(twin,count-1)>changee(tall,count):
            #    return changee(twin,count-1)
            #elif list_to_int(twin)>list_to_int(tall):
                #tall=twin
    if count==0:

    for i in total:
        return changee(i,count-1)
    if len(total)==:
        result=[]
        for i in total:
            result.append(list_to_int(i))
        return max(result)
'''

            
def list_to_int(lii):
    result=""
    for i in lii:
        result=result+str(i)
    return(int(result))


a,b=input().split()
tall=[]
for i in a:
    tall.append(i)
count=int(b)

result1=[]
result2=[]
result3=[]
for k in range(count):

    for i in range(len(tall)):
        for j in range(i+1,len(tall)):
            tall[i],tall[j]=tall[j],tall[i]
            result1.append(tall)
            tall[i],tall[j]=tall[j],tall[i]
        
        






