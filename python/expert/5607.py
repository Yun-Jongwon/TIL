def fac(n) :
    ans = 1 
    if n == 0 :
        return 1 
    else : 
        for i in range(1, n + 1) : 
            ans = ans * i 
        return ans
def com(n, r) :
    return fac(n) / fac(r) / fac(n - r)
    

zxc=int(input())
for i in range (zxc):
    
    a,b=map(int,input().split())
    qwer=1234567891
    if a<=33:
        result=com(a,b)
    else:
        result=com(a,b)**(1/qwer) % qwer
    print(f'#{i+1} {int(result)}')


