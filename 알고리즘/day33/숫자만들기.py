def calculator(data):
    first_number=number[0]
    for d in range(len(data)):
        if data[d]=='+':
            first_number=first_number+number[d+1]
        elif data[d] == '-':
            first_number = first_number - number[d + 1]
        elif data[d] == '*':
            first_number = first_number * number[d + 1]
        elif data[d] == '/':
            first_number = int(first_number / number[d + 1])
    result.append(first_number)


def permu(plus_c,minus_c,star_c,slush_c,data):
    if plus_c==0 and minus_c==0 and star_c==0 and slush_c==0:
        return calculator(data)
    if plus_c>0:
        permu(plus_c-1,minus_c,star_c,slush_c,data+'+')
    if minus_c>0:
        permu(plus_c , minus_c-1, star_c, slush_c, data + '-')
    if star_c>0:
        permu(plus_c , minus_c, star_c-1, slush_c, data + '*')
    if slush_c>0:
        permu(plus_c , minus_c, star_c, slush_c-1, data + '/')




T=int(input())
for t in range(T):
    N=int(input())
    calcul=list(map(int,input().split()))
    number=list(map(int,input().split()))

    result=[]
    permu(calcul[0],calcul[1],calcul[2],calcul[3],'')

    # print(result)
    # # print(min(result))
    # print(start_cal)
    print("#{} {}".format(t+1,max(result)-min(result)))


# 10
# 5
# 2 1 0 1
# 3 5 3 7 9
# 6
# 4 1 0 0
# 1 2 3 4 5 6
# 5
# 1 1 1 1
# 9 9 9 9 9
# 6
# 1 4 0 0
# 1 2 3 4 5 6
# 4
# 0 2 1 0
# 1 9 8 6
# 6
# 2 1 1 1
# 7 4 4 1 9 3
# 7
# 1 4 1 0
# 2 1 6 7 6 5 8
# 8
# 1 1 3 2
# 9 2 5 3 4 9 5 6
# 10
# 1 1 5 2
# 8 5 6 8 9 2 6 4 3 2
# 12
# 2 1 6 2
# 2 3 7 9 4 5 1 9 2 5 6 4