import requests
import bs4

response = requests.get('https://www.naver.com').text
soup = bs4.BeautifulSoup(response,'html.parser')
#result = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(5) > a.ah_a > span.ah_k').text
result = soup.select('div.PM_CL_realtimeKeyword_list_base a.ah_a')
for item in result:
    rank = item.select_one('.ah_r')
    keyword = item.select_one('.ah_k').text
    print(rank )


#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a.ah_a > span.ah_k


