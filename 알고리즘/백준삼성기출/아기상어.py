import collections


def issafe(y, x):
    global N
    if y >= 0 and x >= 0 and y < N and x < N:
        return True
    else:
        return False


N = int(input())
total_map = []
for n in range(N):
    data = list(map(int, input().split()))
    total_map.append(data)
for y in range(N):
    for x in range(N):
        if total_map[y][x] == 9:
            baby_shark = (y, x)
baby_shark_size = 2
baby_shark_eat_count = 0
time = 0
visit = [[-1] * N for i in range(N)]

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

queue = collections.deque([(baby_shark,0)])
blank = collections.deque([])
total_map[baby_shark[0]][baby_shark[1]] = 0
visit[baby_shark[0]][baby_shark[1]] = 0
while queue != blank:
    print(queue)
    # print(visit)
    # print(visit)
    point = queue.popleft()
    # print(total_map)
    # print(point)
    # print(point)
    y = point[0][0]
    x = point[0][1]
    temp=[]
    for dir in range(4):
        if point:


        if issafe(y + dy[dir], x + dx[dir]) and visit[y + dy[dir]][x + dx[dir]] == -1 and total_map[y + dy[dir]][x + dx[dir]] <= baby_shark_size:
            if total_map[y + dy[dir]][x + dx[dir]] < baby_shark_size and total_map[y + dy[dir]][x + dx[dir]] > 0:
                print(baby_shark_size)
                baby_shark_eat_count += 1
                if baby_shark_size == baby_shark_eat_count:
                    baby_shark_size += 1
                    baby_shark_eat_count = 0
                # print(baby_shark_size)

                time += visit[y][x] + 1
                visit = [[-1] * N for i in range(N)]
                baby_shark = (y + dy[dir], x + dx[dir])
                print(baby_shark)

                queue = collections.deque([(baby_shark,0)])
                total_map[y + dy[dir]][x + dx[dir]] = 0
                visit[y + dy[dir]][x + dx[dir]] = 0
                # print(time)
                # print(total_map)
                break

            else:
                if dir == 3:
                    if point[1] == 1 or point[1] == 2:
                        temp.append(((y + dy[dir], x + dx[dir]),3))


                    else:
                        visit[y + dy[dir]][x + dx[dir]] = visit[y][x] + 1
                        # print((y + dy[dir], x + dx[dir]))
                        queue.append(((y + dy[dir], x + dx[dir]),dir))
                else:
                    visit[y + dy[dir]][x + dx[dir]] = visit[y][x] + 1
                    # print((y + dy[dir], x + dx[dir]))
                    queue.append(((y + dy[dir], x + dx[dir]), dir))
    for t in temp:
        if not t in queue:
            queue.append(t)
print(time)






