
for i in range(10):
    a=int(input())
    string=input()
    total=input()
    count=0
    for i in range(len(total)-len(string)+1):
        if total[i:i+len(string)]==string:
            count+=1
    print(f'#{a} {count}')