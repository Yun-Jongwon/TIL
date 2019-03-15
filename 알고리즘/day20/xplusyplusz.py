# data=[]
# def hund(a,b):
#     data.append((a,b))
#     if a==1:
#         new_a=a+1
#         hundleft(new_a,b)
#     if b==49:
#         return
#     else:
#         return hund(a,b+1)

    

# def hundleft(a,b):
#     if 100-(a+b)==b or a==b or a>=33:
#         data.append((a,b))
#         return
#     else:
#         a=a+1
#         data.append((a,b))
#         return hundleft(a,b)
# hund(1,2)
# print(len(data)+1)

Count=0
def xyz(x,y,z):
    global Count
    if x+y+z>100:
        return
    if x>y or y>z or x>z:
        return
    if x+y+z==100:
        Count+=1
        return
    if x+1<=y<=z:
        xyz(x+1,y,z)
    if y+1<=z:
        xyz(x,y+1,z)
    xyz(x,y,z+1)
xyz(1,1,1)
print(Count)
