T=int(input())
for t in range(T):
    string=input()
    stack=[]
    result=0
    for i in string:
        if   (i =="(" or i=="{") :
            stack.append(i)
            continue
        if stack==[] and (i=="}" or i==")"):
            result=-1
            break

        if stack!=[]:
            if (stack[len(stack)-1] !="{" and i=="}") or (stack[len(stack)-1] !="(" and i==")"):
                result=0
                break
            if (stack[len(stack)-1]==")" or stack[len(stack)-1]=="}" or stack==[]) and (i =="(" or i=="{") :
                stack.append(i)
        
            if stack[len(stack)-1] =="(" and i==")":
                stack.pop()
            elif stack[len(stack)-1] =="{" and i=="}":
                stack.pop()

    if result==0 and stack==[]:
        result=1
    else :
        result=0
    print(f'#{t+1} {result}')

    
    