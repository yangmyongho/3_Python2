'''
tag 속성과 내용 가져오기
 - element : tag + tag속성 + tag내용
    ex) <a href="www.naver.com">네이버</a>
    a : tag
    href : tag 속성(attribute)
    네이버 : tag 내용(content)
'''
from bs4 import BeautifulSoup


# 1. local file 가져오기
file = open('./chap08_Crawling/data/html02.html', encoding='utf-8')
src = file.read()


# 2. html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)


# 3. a 태그 앨리먼트 가져오기
links = html.find_all('a') # list 객체
print(links)


# 4. a 태그 -> 속성(href(5개), target(1개))
urls = []
for link in links:
    print(link.string) # tag 내용
    atts = link.attrs # dict
    #print(link.attrs) # tag 속성
    print(atts) # tag 속성 <위아래같음>
    #print(atts['href']) # value  <특정 tag 속성>
    urls.append(atts['href']) # value
    try :
        print(atts['target']) # 오류 : 이 속성이 없는애들이 존재해서
    except Exception as e:
        print('@@@@@@@@@예외발생@@@@@@@ :', e)
print(urls)
# ['www.naver.com', 'http://www.naver.com', 'http://www.naver.com', 'www.duam.net', 'http://www.duam.net']
print(len(urls)) # 5
for i in urls:
    print(i)


# 5. urls -> 정상 url -> new_urls
print('findall 사용')
from re import findall
new_urls = [urls[i] for i in range(len(urls)) if findall('^h',urls[i])]
print(new_urls)




































