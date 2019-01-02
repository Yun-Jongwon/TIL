import webbrowser
import requests


list1=["손흥민","날씨","리버풀"]
for i in list1:
	webbrowser.open('https://search.daum.net/search?q='+i)