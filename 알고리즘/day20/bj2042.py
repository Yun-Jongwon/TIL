def update(a,b):#3,1
    global base
    where=base+a-1
    IDT[where]=b
    where>>=1
    while where:
        IDT[where]=IDT[where*2] + IDT[where*2+1]
        where>>=1
def RSQ(ffrom,tto):
    ffrom=ffrom+base-1
    tto=tto+base-1        
    sum=0
    while ffrom<tto:
        if ffrom&1 :sum+=IDT[ffrom] ;ffrom+=1
        if tto%2==0 : sum+=IDT[tto];tto-=1
        ffrom>>=1
        tto>>=1
    if ffrom==tto:
        sum+=IDT[ffrom]
    print(sum)


N,M,K=map(int,input().split())
howmany=N
base=1
while base < howmany:
    base<<=1
IDT=[0]*(base+howmany)*2


for now in range(base,howmany+base):
    IDT[now]=int(input())
for parent in range(base-1,0,-1):
    IDT[parent]=IDT[parent*2] + IDT[parent*2+1]
for i in range(M+K):
    a,b,c=map(int,input().split())
    if a==1:
        update(b,c)
    else:
        RSQ(b,c)


