import os

os.chdir(r'C:\Users\student\jongwon\day02\dummy')
print(os.getcwd())
for filename in os.listdir('.'):
    os.rename(filename,s)
    s=filename.replace('105_','합격자_105_')