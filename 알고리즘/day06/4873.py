T=int(input())
for t in range(T):
    data=input()
    stack=[]
    for i in range(len(data)):
        if stack==[] or stack[-1]!=data[i]:
            stack.append(data[i])
        else:
            stack.pop()
    print(f'#{t+1} {len(stack)}')

