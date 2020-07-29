'''
원격 서버의 웹문서 수집
'''
from bs4 import BeautifulSoup # source -> html 파싱
import urllib.request as res # 별칭 : 원격 서버 파일 요청
url = 'http://www.naver.com/index.html' # 임의의 주소


# 1. 원격 서버 url 요청
req = res.urlopen(url) # 요청 -> 응답
print(req) # object info  <http.client.HTTPResponse object at 0x0000022D665D2AC8>
data = req.read() # source
print(data) # <!doctype html> -> source


# 2. source(문자열) -> html 형식 : html 파싱
src = data.decode('utf-8') # 디코딩 -> source
html = BeautifulSoup(src, 'html.parser') # source -> html
print(html)


# 3. Tag 내용 가져오기
link = html.find('a') # a 라는 태그 찾기 <a href='url'>내용</a>
# link = html.find_all('a') # a라는 태그 전부 찾기
print(link)
'''
element : <시작태그 속성명='값'>내용</종료태그>
          <a href='url'>내용</a>
'''
print('a 태그 내용', link.string) # 태그 내용 추출
# a 태그 내용 연합뉴스 바로가기














