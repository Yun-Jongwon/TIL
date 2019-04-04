def find_parent_a(start):
    if start==1 or start==0:
        return
    a_parent.append(parent[start])
    return find_parent_a(parent[start])
def find_parent_b(start):
    global com_parent
    if start==1 or start==0:
        return
    # b_parent.append(parent[start])
    if parent[start] in a_parent:
        com_parent=parent[start]
        return
    else:
        return find_parent_b(parent[start])

def dfs(com_parent):
    global child_count


    if child[com_parent] !=[]:
        child_count+=len(child[com_parent])
        for i in child[com_parent]:
            dfs(i)



T=int(input())
for t in range(T):
    V,E,a,b=map(int,input().split())
    data=list(map(int,input().split()))
    child=[[] for v in range(V+1)]
    parent=[0]*(V+1)
    a_parent=[]
    # b_parent=[]

    for e in range(E):
        child[data[2*e]].append(data[2*e+1])
        parent[data[2*e+1]]=data[2*e]
    # print(parent)
    find_parent_a(a)
    find_parent_b(b)
    child_count=0
    # print(a_parent)
    # print(b_parent)

    # for i in range(len(a_parent)):
    #     if a_parent[i] in b_parent:
    #         com_parent=a_parent[i]
    #         break
    dfs(com_parent)
    print("#{} {} {}".format(t+1,com_parent,child_count+1))





