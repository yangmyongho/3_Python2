'''
선택자(selector)
 - 웹 문서 디자인(css)에서 사용
 - 선택자 : id(#) : 중복불가 , class(.) : 중복가능
 - html.select('선택자') : 여러개 element 수집
 - html.select_one('선택자') : 한개 element 수집
'''
from bs4 import BeautifulSoup


# 1. 태그 & 선택자
file = open('chap08_Crawling/data/html03.html', encoding='utf-8')
src = file.read()
print(src)
html = BeautifulSoup(src, 'html.parser')

# 1-1) id 선택자 : #
table = html.select_one('#tab') # id = 'tab'
print(table) # <table> ~ </table>
# <table> <tr> <th> or <td>  계층적 접근
ths = html.select('#tab > tr > th') # list
print(ths)
print(len(ths)) # 4
for th in ths:
    print(th.string) # tag 내용

# 1-2) class 선택자 : .
trs = html.select('#tab > .odd') # 5개<tr> 중에 -> 2개<tr> 꺼내옴
print(trs)
for tr in trs :
    #print(tr)
    tds = tr.find_all('td') # list
    for td in tds:
        print(td.string)

# 1-3) tag[속성='값'] 찾기
trs = html.select('tr[class="odd"]')
print(trs)
for tr in trs :
    tds = tr.find_all('td') # list
    for td in tds:
        print(td.string)












