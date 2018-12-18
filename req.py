import requests
import bs4

response = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(response,'html.parser')
result = soup.select_one('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(5) > a.ah_a > span.ah_k').text

print('현재 원/달러 환율은 '+ result + '입니다.')

print('현재 원/달러 환율은  {} 입니다.'.format(result))