'''
get  vs  post
 - 파라미터 전송 방식
 - get : url에 노출(소량의데이터)
 - post : body에 포함되어 전송(대량의데이터)

 <작업순서>
 1. index 페이지 : 메뉴 선택(radio or select) -> get 방식
 2. flask server 파라미터 받기(메뉴 번호)
 3. 메뉴 번호에 따라서 각 페이지로 이동
'''
from flask import Flask, render_template, request
# db 연결 객체 생성 함수
def db_conn():
    import pymysql
    config = {'host': '127.0.0.1', 'user': 'scott', 'password': 'tiger',
                'database': 'work', 'port': 3306, 'charset': 'utf8', 'use_unicode': True}
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    return conn, cursor
# 결과 조회 함수
def select_func():
    sql = "select * from goods"
    conn, cursor = db_conn() # db 연동 객체 생성
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close(); conn.close()
    return data



app = Flask(__name__) # object -> app object

# 함수 장식자
@app.route('/') # http://127.0.0.1:5000
def index():
    return render_template("/app04/index.html")

@app.route('/select', methods = ['GET', 'POST']) # http://127.0.0.1:5000/select?menu=1&name=홍길동
def select():
    if request.method == 'GET':
        menu = int(request.args.get('menu'))
        #name = request.args.get('name') # 2개 이상일경우 이렇게 쓰면된다.
        # print('menu :', menu) # 잘넘어가나 확인
        if menu == 1 : # 전체 메뉴 조회
            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)
        if menu == 2 : # 메뉴 추가
            return render_template("/app04/insert_form.html")
        if menu == 3 : # 메뉴 수정
            return render_template("/app04/update_form.html")
        if menu == 4 : # 메뉴 삭제
            return render_template("/app04/delete_form.html")

@app.route("/insert", methods = ['GET', 'POST'])
def insert():
    try:
        if request.method == 'POST':
            code = int(request.form['code'])
            name = request.form['name']
            su = int(request.form['su'])
            dan = int(request.form['dan'])
            # 레코드 삽입
            conn,cursor = db_conn()
            sql = f"insert into goods values({code},'{name}',{su},{dan})"
            cursor.execute(sql)
            conn.commit()
            cursor.close(); conn.close()
            # 결과 조회
            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)
    except Exception as e:
        return render_template("app04/error.html", error_info = e)

@app.route("/update", methods = ['GET', 'POST'])
def update():
    try:
        if request.method == 'POST':
            code = int(request.form['code'])
            #name = request.form['name']
            su = int(request.form['su'])
            dan = int(request.form['dan'])
            # 레코드 수정
            conn,cursor = db_conn()
            sql = f"update goods set su ={su}, dan={dan} where code={code}"
            cursor.execute(sql)
            conn.commit()
            cursor.close(); conn.close()
            # 결과 조회
            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)
    except Exception as e:
        return render_template("app04/error.html", error_info = e)

@app.route("/delete", methods = ['GET', 'POST'])
def delete():
    try:
        if request.method == 'GET':
            code = int(request.args.get('code'))
            # 레코드 삭제
            conn,cursor = db_conn()
            sql = f"delete from goods where code = {code}"
            cursor.execute(sql)
            conn.commit()
            cursor.close(); conn.close()
            # 결과 조회
            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)
    except Exception as e:
        return render_template("app04/error.html", error_info = e)


# 프로그램 시작점
if __name__ == "__main__" :
    app.run() # application 실행


#return render_template(menu=menu)