def shap(x,y):
    result=0
    for i in range(1,x+1):
        result=result+i
    for j in range(y-1):
        if y==1:
            break
        result=result+x+j
    
    return result




def ad(ro):
    count=0
    first=ro
    for k in range(1,10000):
        ro=ro-k
        count+=1
        if ro<=0:
            break
    print(count)
    for i in range(1,count+1):
        
        if shap(i,count+1-i)==int(first):
            return (i,count+1-i)
            
            


        

print(ad(9))

print((3,2)+(2,2))