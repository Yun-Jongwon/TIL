def dfs(next, cnt):
    global minimum
    if cnt == N // 2:
        # print(visited)

        resulty = 0
        resultx = 0

        for n in range(N):
            if visited[n]==1:
                resulty += total_map[n][0]
                resultx += total_map[n][1]
            else:
                resulty -= total_map[n][0]
                resultx -= total_map[n][1]

        result = resulty ** 2 + resultx ** 2
        if minimum > result:
            minimum = result
        return

    for i in range(next, N):
        if not visited[i]:
            visited[i] = 1
            dfs(i + 1, cnt + 1)
            visited[i] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    total_map = []
    for n in range(N):
        data = list(map(int, input().split()))
        total_map.append(data)

    visited = [0] * N
    minimum = 80000000000
    visited[0]=1
    dfs(1, 1)
    print("#%d %d" % (tc + 1, minimum))
