import requests
import bs4

response = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(response,'html.parser')
result = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text

print('현재 원/달러 환율은 '+ result + '입니다.')

print('현재 원/달러 환율은  {} 입니다.'.format(result))