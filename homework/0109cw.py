

# 이분법을 통한 제곱근 구하기
def ban(x,y):
    inx=y
    if round(x,20)==round(y,20):
        return f'{x}< sqrt < {y}'

    if x**2<inx and inx<y**2:
        return ban(x,round((x+y)/2,20))
    else:
        return ban(y,round(y*2-x,20))



print(ban(1,4))
print(2**(1/2))

#강사님 버전
def my_sqrt(n):
    x,y=1,n
    result=1
    #while not math.isclose(result**2,n)
    while abs(result**2-n)>0.000001:
        result=(x+y)/2
        if result**2<n:
            x=result
        else:
            y=result
    return result