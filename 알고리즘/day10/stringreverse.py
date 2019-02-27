s='algorithm'
n=""
for i in range(-1,-len(s)-1,-1):
    n+=s[i]
    # print(n)





# atoi 16진수 42FB
s='42FB'
total_result=0
for j in range(-1,-len(s)-1,-1):
    i=-j-1
    if ord('A')<ord(s[j]) and ord(s[j])<ord('Z'):
        result=ord(s[j])-ord('A')
        # print(result)
        total_result+=(result+10)*(16**i)
        # print(i)
        # print(total_result)
    elif ord('0')<ord(s[j]) and ord(s[j])<ord('9'):
        result=ord(s[j])-ord('0')
        total_result+=result*(16**i)
    # print(total_result)
print(total_result)



# itoa
s=123
namuzi=123
result=''
while namuzi!=0:
    namuzi=s%10
    if namuzi==0:
        break
    s=s//10
    print(namuzi)
    # print(ord('0'))
    result+=chr(namuzi+ord('0'))
s=result
n=""
for i in range(-1,-len(s)-1,-1):
    n+=s[i]
    print(n)




