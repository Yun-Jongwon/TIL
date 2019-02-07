
hwaro=[]
hwaro_size=int(input())
pizza=list(map(int,input().split()))
pizza_number=[]

hwaro_number=[]


for i in range(len(pizza)):
    pizza_number.append(i)

for i in range(hwaro_size):
    hwaro.append(pizza.pop(0))
    hwaro_number.append(pizza_number.pop(0))




while len(hwaro)>1:

    a=hwaro.pop(0)
    b=a//2

    if b!=0:
        hwaro.append(b)
        hwaro_number.append(hwaro_number.pop(0))

    else:
        if pizza!=[]:
            hwaro.append(pizza.pop(0))
        hwaro_number.pop(0)
        if pizza_number!=[]:
            hwaro_number.append(pizza_number.pop(0))

print(hwaro_number[0]+1)
    

        