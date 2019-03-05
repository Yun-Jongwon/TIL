T=int(input())
for t in range(T):
    N,L,K=map(int,input().split())
    position=[0]*(L+1)
    for n in range(N):
        p,I=int(input().split())
        position[I]=p
    len_position=len(position)
    for i in range(len_position//2):
        position[i]
        position[len_position-i-1]


    if 왼쪽 끝이 - 이고 오른쪽 끝이 +일때 까지 변형시키기
    좌우중에 가까운것 1개넣고 다시비교







