'''
 문) login.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오. 
    조건1> id="login_wrap" 선택자의  하위 태그  전체 출력 
    조건2> id="login_warp" 선택자  > form > table 태그 내용 출력 
    조건3> find_all('tr') 함수 이용  th 태그 내용 출력  
'''

from bs4 import BeautifulSoup

# 1. html source 가져오기 
file = open('chap08_Crawling/data/login.html', encoding='utf-8')
src = file.read()
# 2. html 파싱
html = BeautifulSoup(src, 'html.parser')
# 3. 선택자 이용 태그 내용 가져오기 
log = html.select('#login_wrap')
print(log)

log2 = html.select_one('#login_wrap > form > table')
print(log2)

log3 = html.find_all('tr')
for log4 in log3:
    log5 = log4.find_all('th')
    for log6 in log5:
        print(log6.string)




