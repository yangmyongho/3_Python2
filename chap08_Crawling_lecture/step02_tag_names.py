'''
tag 명으로 찾기
 형식)
    html.find('tag') : 최초로 발견된 tag 1개 수집
    html.find_all('tag') : 해당 tag 전체 수집
'''
from bs4 import BeautifulSoup # html 파싱


# 1. local file 불러오기
file = open('./chap08_Crawling/data/html01.html', mode='r', encoding='utf-8')
src = file.read()
print(src)


# 2. src -> html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)

# 3. tag 찾기 -> 내용 추출
# 3-1) tag 계층적 구조
h1 = html.html.body.h1  # <h1>
print(h1) # element : <h1> 시멘틱 태그 ?</h1>
print(h1.string) # 내용 : 시멘틱 태그 ?

# 3-2) find('tag')
h2 = html.find('h2') # <h2>
print(h2) # element : <h2> 주요 시멘틱 태그 </h2>
print(h2.string) # 내용 : 주요 시멘틱 태그

# 3-3) find_all('tag') # list 구조 <원소가 2개이상이면 list나 tuple구조이다>
lis = html.find_all('li')
print(lis) # list
# [<li> header : 문서의 머리말(사이트 소개, 제목, 로그 )</li>, <li> nav : 네이게이션(메뉴) </li>, ]
print(len(lis)) # 5
print(lis[0].string) #  header : 문서의 머리말(사이트 소개, 제목, 로그 )
for li in lis :
    print(li.string)
li_cont = [li.string for li in lis]
print(li_cont)















