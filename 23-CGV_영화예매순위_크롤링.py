import urllib.request as req
from bs4 import BeautifulSoup

# 서버한테 HTML 코드 받기
code = req.urlopen("http://www.cgv.co.kr/movies/")
# print(code.read())

# HTML 코드 예쁘게 정리하기
soup = BeautifulSoup(code, "html.parser")
# print(soup)

# 내가 원하는 요소 찾게하기
# title = soup.select_one("strong.title") #요소 하나만 가져옴!
title = soup.select("strong.title") #요소 여러개 한번에!

# 요소의 내용 출력하기
for i in title:
    print(i.string) # 요소 내용 꺼내오기