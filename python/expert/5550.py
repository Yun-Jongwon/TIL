string=input()
c=[]
r=[]
o=[]
a=[]
k=[]

for i in string:
    if i =='c':
        c.append(i)

    if i == 'r':
        if len(c)>len(r):
            r.append(i)
        else:
            break

    if i == 'o':
        if len(r)>len(o):
            o.append(i)
        else:
            break

    if i == 'a':
        if len(o)>len(a):
            a.append(i)
        else:
            break

    if i == 'k':
        if len(a)>len(k):
            k.append(i)
        else:
            break

if len(c)==len(r)==len(o)==len(a)==len(k):
    print(len(k))
else:
    print(-1)
    
