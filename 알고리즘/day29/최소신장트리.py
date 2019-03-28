# import sys
# sys.stdin = open("input.txt")


def find(x):
    if x != parent[x]: #조상 찾기
        return find(parent[x])
    else: #자신이랑 엄마가 같으면 즉, 자신이 엄마면
        return parent[x]

def union(x,y,z):
    global ans, cnt
    x = find(x) #x엄마 찾기
    y = find(y)
    if x!=y: #엄마가 다르면
        parent[find(x)]=find(y) #y의 엄마가 x가 됨
        ans += z
        cnt += 1

for tc in range(int(input())):
    n,p = map(int,input().split())
    node = [0]*(n+1)
    datas = []
    for i in range(n+1):
        node[i] = i #노드 만들기

    parent = [0]*(n+1) #엄마 지정해주기
    for make in range(n+1): #우선 엄마는 자기 자신
        parent[make] = make
    # print(parent)

    for ii in range(p):
        datas.append(list(map(int,input().split())))
    # print(datas)
    datas.sort(key=lambda x: x[2]) #2차원 리스트의 인덱스2의 값으로 오름차순
    # print(datas)

    ans = 0
    cnt = 0
    # print(datas)
    for path in datas:
        # print(path)
        union(path[0],path[1],path[2])
        if cnt == n:
            break
    print('#{} {}'.format(tc+1,ans))
# 4 5
# 0 1 10
# 0 2 7
# 1 4 2
# 2 3 10
# 2 4 3