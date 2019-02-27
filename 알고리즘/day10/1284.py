T=int(input())
for t in range(T):
    P,Q,R,S,W=map(int,input().split())
    A=W*P
    if W<=R:
        B=Q
    else:
        B=Q+(W-R)*S
    if A>=B:
        print(f'#{t+1} {B}')
    else:
        print(f'#{t+1} {A}')