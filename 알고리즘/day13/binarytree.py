data=[1,2,1,3,2,4,3,5,3,6,4,7,5,8,5,9,6,10,6,11,7,12,11,13]
leftchild=[0]*14
rightchild=[0]*14
child_count=[0]*14
parent=[0]*14
level=[0]*14


for i in range(len(data)//2):
    p=data[2*i]
    c=data[2*i+1]
    if child_count[p]==0:
        leftchild[p]=c
    else:
        rightchild[p]=c
    child_count[p] += 1
    level[c] = level[p] + 1
    parent[c] = p

tree=list(map(list,zip(leftchild,rightchild,child_count,parent,level)))
for i in tree:
    print(i)
def preorder(T):
    if T:
        print('%d'%T,end=' ')
        preorder(tree[T][0])
        preorder(tree[T][1])
preorder(1)
print()
def postorder(T):
    if T:
        postorder(tree[T][0])
        postorder(tree[T][1])
        print('%d'%T,end=' ')
postorder(1)
print()
def inorder(T):
    if T:
        inorder(tree[T][0])
        print('%d'%T,end=' ')
        inorder(tree[T][1])
inorder(1)
print()


print(level)
# for i in range(1,max(level)):







p_13=13
result=0
while result!=1:
    p_13=parent[p_13]
    print(p_13,end=" ")
    result=p_13