T=int(input())
for t in range(T):
    string=input()
    length=len(string)
    first_line='..#.'
    second_line='.#'
    for i in range(length):
        print(first_line,end='')
    print('.')

    for i in range(length):
        print(second_line*2,end='')
    print('.')

    for i in range(length):
        print('#.',end='')
        print(string[i],end='')
        print('.',end='')
    print('#')

    for i in range(length):
        print(second_line*2,end='')
    print('.')

    for i in range(length):
        print(first_line,end='')
    print('.')