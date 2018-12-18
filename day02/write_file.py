# f=open('ssafy.txt','w')#w:write, r:read, a:append
# f.write('this is ssafy!!!!?!?!?!?!?')
# f.close()

with open('ssafy.txt','w',encoding='utf8') as f:

    f.writelines(['1\n','2\n','3\n'])

    # for i in range(10):
    #     f.write(f'this is ssafy\\ \' \" \"!!!!?!?!?!?!?{i}\n')
    #     #\t : tab ,
    #     #  \\ : \,
    #     #   \' \"  : ' "
    #     f.write('이건사피인가!!!!?!?!?!?!?')

