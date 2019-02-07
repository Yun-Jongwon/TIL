T = int(input())
for t in range(T):
    goo = []
    option = list(map(int, input().split()))
    dy = option[0]
    dx = option[1]
    for i in range(dy):
        goo.append(list(map(int, input().split())))

    start = [option[2], option[3]]
    time = option[4]
    queue = []
    queue.append(start)

    right = [1, 3, 6, 7]
    left = [1, 3, 4, 5]
    up = [1, 2, 5, 6]
    down = [1, 2, 4, 7]
    result = []

    for j in range(time):
        if queue == []:
            break
        for i in range(len(queue)):
            present = queue.pop(0)
            result.append(present)
            y = present[0]
            x = present[1]
            try:
                if queue == []:
                    if goo[y][x] == 1:
                        if goo[y][x+1] in right:
                            queue.append([y, x+1])
                            goo[y][x] = -1
                        if goo[y+1][x] in down:
                            queue.append([y+1, x])
                            goo[y][x] = -1
                        if goo[y][x-1] in left and x-1 >= 0:
                            queue.append([y, x-1])
                            goo[y][x] = -1
                        if goo[y-1][x] in up and y-1 >= 0:
                            queue.append([y-1, x])
                            goo[y][x] = -1
                    if goo[y][x] == 2:
                        if goo[y+1][x] in down:
                            queue.append([y+1, x])
                            goo[y][x] = -1
                        if goo[y-1][x] in up and y-1 >= 0:
                            queue.append([y-1, x])
                            goo[y][x] = -1
                    if goo[y][x] == 3:
                        if goo[y][x+1] in right:
                            queue.append([y, x+1])
                            goo[y][x] = -1
                        if goo[y][x-1] in left and x-1 >= 0:
                            queue.append([y, x-1])
                            goo[y][x] = -1
                    if goo[y][x] == 4:
                        if goo[y][x+1] in right:
                            queue.append([y, x+1])
                            goo[y][x] = -1
                        if goo[y-1][x] in up and y-1 >= 0:
                            queue.append([y-1, x])
                            goo[y][x] = -1
                    if goo[y][x] == 5:
                        if goo[y][x+1] in right:
                            queue.append([y, x+1])
                            goo[y][x] = -1
                        if goo[y+1][x] in down:
                            queue.append([y+1, x])
                            goo[y][x] = -1
                    if goo[y][x] == 6:
                        if goo[y+1][x] in down:
                            queue.append([y+1, x])
                            goo[y][x] = -1
                        if goo[y][x-1] in left and x-1 >= 0:
                            queue.append([y, x-1])
                            goo[y][x] = -1
                    if goo[y][x] == 7:
                        if goo[y-1][x] in up and y-1 >= 0:
                            queue.append([y-1, x])
                            goo[y][x] = -1
                        if goo[y][x-1] in left and x-1 >= 0:
                            queue.append([y, x-1])
                            goo[y][x] = -1

        ######################################
                else:
                    if goo[y][x] == 1:
                        if [y-1, x] in result:
                            if goo[y][x+1] in right:
                                queue.append([y, x+1])
                                goo[y][x] = -1
                            if goo[y+1][x] in down:
                                queue.append([y+1, x])
                                goo[y][x] = -1
                            if goo[y][x-1] in left and x-1 >= 0:
                                queue.append([y, x-1])
                                goo[y][x] = -1
                        if [y, x+1] in result:
                            if goo[y-1][x] in up and y-1 >= 0:
                                queue.append([y-1, x])
                                goo[y][x] = -1
                            if goo[y+1][x] in down:
                                queue.append([y+1, x])
                                goo[y][x] = -1
                            if goo[y][x-1] in left and x-1 >= 0:
                                queue.append([y, x-1])
                                goo[y][x] = -1
                        if [y+1, x] in result:
                            if goo[y-1][x] in up and y-1 >= 0:
                                queue.append([y-1, x])
                                goo[y][x] = -1
                            if goo[y][x+1] in right:
                                queue.append([y, x+1])
                                goo[y][x] = -1
                            if goo[y][x-1] in left and x-1 >= 0:
                                queue.append([y, x-1])
                                goo[y][x] = -1
                        if [y, x-1] in result:
                            if goo[y-1][x] in up and y-1 >= 0:
                                queue.append([y-1, x])
                                goo[y][x] = -1
                            if goo[y+1][x] in down:
                                queue.append([y+1, x])
                                goo[y][x] = -1
                            if goo[y][x+1] in right:
                                queue.append([y, x+1])
                                goo[y][x] = -1

                    if goo[y][x] == 2:
                        if [y-1, x] in result:
                            if goo[y+1][x] in down:
                                queue.append([y+1, x])
                                goo[y][x] = -1
                        if [y+1, x] in result:
                            if goo[y-1][x] in up and y-1 >= 0:
                                queue.append([y-1, x])
                                goo[y][x] = -1
                    if goo[y][x] == 3:
                        if [y, x-1] in result:
                            if goo[y][x+1] in right:
                                queue.append([y, x+1])
                                goo[y][x] = -1
                        if [y, x+1] in result:
                            if goo[y][x-1] in left and x-1 >= 0:
                                queue.append([y, x-1])
                                goo[y][x] = -1
                    if goo[y][x] == 4:
                        if [y-1, x] in result:
                            if goo[y][x+1] in right:
                                queue.append([y, x+1])
                                goo[y][x] = -1
                        if [y, x+1] in result:
                            if goo[y-1][x] in up and y-1 >= 0:
                                queue.append([y-1, x])
                                goo[y][x] = -1
                    if goo[y][x] == 5:
                        if [y+1, x] in result:
                            if goo[y][x+1] in right:
                                queue.append([y, x+1])
                                goo[y][x] = -1
                        if [y, x+1] in result:
                            if goo[y+1][x] in down:
                                queue.append([y+1, x])
                                goo[y][x] = -1
                    if goo[y][x] == 6:
                        if [y, x-1] in result:
                            if goo[y+1][x] in down:
                                queue.append([y+1, x])
                                goo[y][x] = -1
                        if [y+1, x] in result:
                            if goo[y][x-1] in left and x-1 >= 0:
                                queue.append([y, x-1])
                                goo[y][x] = -1
                    if goo[y][x] == 7:
                        if [y, x-1] in result:
                            if goo[y-1][x] in up and y-1 >= 0:
                                queue.append([y-1, x])
                                goo[y][x] = -1
                        if [y-1, x] in result:
                            if goo[y][x-1] in left and x-1 >= 0:
                                queue.append([y, x-1])
                                goo[y][x] = -1
            print(queue)
            print(goo)
    final = []
    for i in result:
        if i not in final:
            final.append(i)

    print(f'#{t+1} {len(final)}')
