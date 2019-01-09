# #
def shap(li):
    x=li[0]
    y=li[1]
    result=0
    for i in range(1,x+1):
        result=result+i
    for j in range(y-1):
        if y==1:
            break
        result=result+x+j
    
    return result
# &
def ad(ro):
    count=0
    first=ro
    for k in range(1,10000):
        ro=ro-k
        count+=1
        if ro<=0:
            break
    for i in range(1,count+1):
        
        if shap([i,count+1-i])==int(first):
            return [i,count+1-i]
            
            
def plus(a,b):
    c=a[0]+b[0]
    d=a[1]+b[1]
    return [c,d]

T=int(input())
for i in range(T):
    a,b=map(int,input().split())  
    print(f'#{i+1} {shap(plus(ad(a),ad(b)))}')
