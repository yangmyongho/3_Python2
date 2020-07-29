'''
python 객체(list, dict) -> 템플릿으로 보내기

JinJa2 템플릿 표현식
    {{ object }} : 단일 객체 출력
    {% for 변수 in 열거형객체 %} : 열거형 객체 출력
    {% if: True    else: False %} : 논리적
'''
from flask import Flask, render_template # app 생성, html 호출


app = Flask(__name__) # object -> app object

# 함수 장식자
@app.route('/') # 기본 url 요청 -> 함수 호출
def index():
    return render_template("/app02/index.html")

@app.route('/temp01') # 기본 url/temp01 요청 -> 함수 호출
def temp01():
    # python object
    uname = '홍길동' # 단일객체
    goodsList = ['딸기', '포도', '사과'] # 열거형객체
    return render_template("/app02/temp01_page.html", name=uname, glist=goodsList)

@app.route('/temp02/<uname>') # 기본 url/temp01/홍길동
def temp02(uname):
    return render_template("/app02/temp02_page.html", name=uname)


# 프로그램 시작점
if __name__ == "__main__" :
    app.run() # application 실행

