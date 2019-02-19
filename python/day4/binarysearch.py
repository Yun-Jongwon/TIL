T = int(input())
for t in range(T):
    total_page, A_target, B_target = map(int, input().split())
    A_start = B_start = 0
    A_end = B_end = total_page
    A_center = (A_start + A_end) // 2
    B_center = (B_start + B_end) // 2
    while True:
        A = 0
        B = 0
        if A_start == A_target or A_end == A_target:
            A = 1
        if A_target > A_center:
            A_start = A_center
            A_center = (A_start + A_end) // 2
        elif A_target < A_center:
            A_end = A_center
            A_center = (A_start + A_end) // 2
        elif A_target == A_center:
            A = 1

        if B_start == B_target or B_end == B_target:
            B = 1
        if B_target > B_center:
            B_start = B_center
            B_center = (B_start + B_end) // 2
        elif B_target < B_center:
            B_end = B_center
            B_center = (B_start + B_end) // 2
        elif B_target == B_center:
            B = 1

        if A == 1 and B == 0:
            print(f'#{t + 1} A')
            break
        elif A == 0 and B == 1:
            print(f'#{t + 1} B')
            break
        elif A == 1 and B == 1:
            print(f'#{t + 1} 0')
            break



