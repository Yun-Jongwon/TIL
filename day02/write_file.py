# f=open('ssafy.txt','w')#w:write, r:read, a:append
# f.write('this is ssafy!!!!?!?!?!?!?')
# f.close()

with open('ssafy.txt','w',encoding='utf8') as f:
    f.write('this is ssafy!!!!?!?!?!?!?')
    f.write('이건사피인가!!!!?!?!?!?!?')

