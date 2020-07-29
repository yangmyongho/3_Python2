'''
1. news Crawling
    url : http://media.daum.net
2. pickle save
    binary file save
'''
import urllib.request as req # url 요청
from bs4 import BeautifulSoup # html 파싱
import pickle


# 1. url = 'http://media.daum.net'
url = 'http://media.daum.net'

# 1-1) url 요청
res = req.urlopen(url)
src = res.read() # source
print(src)

# 1-2) html 파싱
de_src = src.decode('utf-8') # 디코딩
html = BeautifulSoup(de_src, 'html.parser')
print(html)

# 1-3) tag[속성='값'] -> "a[class='link_txt']"
links = html.select("a[class='link_txt']")
print(len(links)) # 62
print(links)

# 1-4) 기사 내용만 추출
crawling_data = [] # 빈 list
for link in links:
    link_str = str(link.string) # 내용만 추출후 문자타입으로 변경
    crawling_data.append(link_str.strip()) # 문장끝 불용어 처리(\n, 공백) , 빈 list에 삽입
print(crawling_data)
print(len(crawling_data)) # 62
cnt = 0
for i in crawling_data:
    cnt += 1
    print(cnt, i)

# 1-5) pickle file save
file = open('chap08_Crawling/data/new_crawling.pickle', mode='wb')
pickle.dump(crawling_data, file)















