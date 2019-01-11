sosu=[2]
for i in range(2,1000001):
    rl=True
    for j in sosu:
        if i%j==0:
            rl=False           
            break
    if rl:
        sosu.append(i)
print(sosu)
            	