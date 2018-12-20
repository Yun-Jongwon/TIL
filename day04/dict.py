

lunch={
    '중국집':'054-111-2222',
    '양식집':'054-222-3333',
    '한식집':'054-777-6666',





}

dinner = dict(돈가스="02-13-132")

# 2. 딕셔너리에 내용 추가
lunch['분식집']='053-877-5858'
# 3. 딕셔너리 내용 가져오기

print(lunch['중국집'])

#3.1
idol={
    'bts':{'지민':24,'RM':25}

}

print(idol['bts']['RM'])



# 4. 딕셔너리 반복문 활용하기

for key in lunch :
    print(key)
    print(lunch[key])

# key만 가져오기 : .keys
for key in lunch.keys():
    print(key)


# vlalue만 가져오기 : .values()
for value in lunch.values():
    print(value)

# item 가져오기(key,value) : .items() => 튜플로 들어옴
for key, value in lunch.items():
    print(key,value)


# 퀴즈 1
score ={
    '수학':90,
    '국어':90,
    '음악':100
}
total=0
for key in score:
    total=total+score[key]

print(total/len(score))



# 퀴즈 2 반평균
score ={'a':{'수학':80,'국어':90,'음악':100},
    
    
    'b': { '수학':90,'국어':80,'음악':100}
}




total=0

#for i in score :
 #   for key in score[i]:
  #      total=total+score[i][key]




for i in score.values() :
    total+=sum(i.values())    

#print(total/6)
leng=len(score)*len(i.values())
print(total/leng)










####도시별 최근 3일의 온도

city={
    '서울':[-6,-10,6],
    '대전':[-3,-10,6],
    '광주':[0,-2,10],
    '구미':[2,-2,9]
}
##도시별 최근 3일 의 온도 평균


for i in city.keys() :
    print(f'{i} : {sum(city[i])/len(city[i])}도')




for name, temp in city.items():
    aver=sum(temp)/len(temp)
    print(f'{name} : {aver}')



