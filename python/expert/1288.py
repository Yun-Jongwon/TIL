n=int(input())
for i in range(n)  :
    shn=input()
    cal=int(shn)
    sh=list(shn)
    set2=set(sh)
    if len(set2)==10:
        break
    count=2
    while len(set2)<10 :
        real_shn=cal*count
        real_sh=str(real_shn)
        set3=set(real_sh)
        set2=set2|set3
        count+=1
    print(f'#{i+1} {real_shn}')
        

