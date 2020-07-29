# Hospital Info
from flask import Flask, render_template, request
# db 연결 객체 생성 함수
def db_conn():
    import pymysql
    config = {'host': '127.0.0.1', 'user': 'scott', 'password': 'tiger',
                'database': 'work', 'port': 3306, 'charset': 'utf8', 'use_unicode': True}
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    return conn, cursor

app = Flask(__name__) # object -> app object
# 함수 장식자
@app.route('/') # http://127.0.0.1:5000
def index():
    return render_template("/app05/main.html")

@app.route('/docForm')
def docForm():
    return render_template("/app05/docForm.html")

@app.route('/docPro', methods = ['GET', 'POST'])
def docPro():
    if request.method == 'POST':
        doc_id = int(request.form['id'])
        major = request.form['major']
        conn,cursor = db_conn()
        sql = f"select *from doctors where doc_id = {doc_id} and major_treat = '{major}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row: # login 성공 -> 진료정보
            sql = f"""select d.doc_id, t.pat_id, TREAT_CONTENTS, TREAD_DATE 
            from doctors d inner join treatments t
            on d.doc_id = t.doc_id and d.doc_id = {doc_id}"""
            cursor.execute(sql)
            data = cursor.fetchall()
            size = len(data)
            return render_template("/app05/docPro.html", dataset = data, size = size)
        else: # login 실패
            return render_template("/app05/error_doc.html", info ="id 또는 진료과목 확인")

@app.route('/nurseForm')
def nurseForm():
    return render_template("/app05/nurseForm.html")

@app.route('/nursePro', methods = ['GET', 'POST'])
def nursePro():
    if request.method == 'POST' :
        nur_id = int(request.form['id'])
        conn, cursor = db_conn()
        sql = f"select *from nurses where nur_id = {nur_id}"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            sql = f"""select n.NUR_ID, DOC_ID, PAT_ID, PAT_PHONE
            from nurses n inner join patients p
            on n.nur_id = p.nur_id and n.nur_id = {nur_id}"""
            cursor.execute(sql)
            data = cursor.fetchall()
            size = len(data)
            return render_template("/app05/nursePro.html", dataset=data, size=size)
        else:
            return render_template("/app05/error_nur.html", info="id 확인")

# 프로그램 시작점
if __name__ == "__main__" :
    app.run() # application 실행
