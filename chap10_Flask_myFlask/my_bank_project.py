# Bank Info
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
    return render_template("/my/main.html")

@app.route('/bankForm')
def bankForm():
    return render_template("/my/bankForm.html")

@app.route('/bankPro', methods = ['GET', 'POST'])
def bankPro():
    if request.method == 'POST':
        bcode = int(request.form['code'])
        conn,cursor = db_conn()
        sql = f"select *from bank where bcode = {bcode}"
        cursor.execute(sql)
        row = cursor.fetchall()
        if row:
            sql = f"""select b.bcode, b.bname, b.bjoin, d.ycode, d.yname, d.period, d.rate 
            from bank b inner join deposit d
            on b.bcode = d.bcode and b.bcode = {bcode}"""
            cursor.execute(sql)
            data = cursor.fetchall()
            size1 = len(data)
            sql = f"""select b.bcode, b.bname, b.bjoin, s.jcode, s.jname, s.period, s.rate 
            from bank b inner join saving s
            on b.bcode = s.bcode and b.bcode = {bcode}"""
            cursor.execute(sql)
            data2 = cursor.fetchall()
            size2 = len(data2)
            return render_template("/my/bankPro.html", dataset = data, dataset2=data2, size1 = size1, size2=size2 )
        else: # login 실패
            return render_template("/my/error_bank.html", info ="은행명 확인")

@app.route('/depositForm')
def depositForm():
    return render_template("/my/depositForm.html")

@app.route('/depositPro', methods = ['GET', 'POST'])
def depositPro():
    if request.method == 'POST':
        ycode = int(request.form['code'])
        conn,cursor = db_conn()
        sql = f"select *from deposit where ycode = {ycode}"
        cursor.execute(sql)
        row = cursor.fetchall()
        if row:
            sql = f"""select b.bcode, b.bname, b.bjoin, d.ycode, d.yname, d.period, d.rate 
            from bank b inner join deposit d
            on b.bcode = d.bcode and d.ycode = {ycode}"""
            cursor.execute(sql)
            data = cursor.fetchall()
            size = len(data)
            return render_template("/my/depositPro.html", dataset = data, size=size)
        else :
            return render_template("/my/error_deposit.html", info="예금코드 확인")

@app.route('/savingForm')
def savingForm():
    return render_template("/my/savingForm.html")

@app.route('/savingPro', methods = ['GET', 'POST'])
def savingPro():
    if request.method == 'POST':
        jcode = int(request.form['code'])
        conn,cursor = db_conn()
        sql = f"select *from saving where jcode = {jcode}"
        cursor.execute(sql)
        row = cursor.fetchall()
        if row:
            sql = f"""select b.bcode, b.bname, b.bjoin, s.jcode, s.jname, s.period, s.rate 
            from bank b inner join saving s
            on b.bcode = s.bcode and s.jcode = {jcode}"""
            cursor.execute(sql)
            data = cursor.fetchall()
            size = len(data)
            return render_template("/my/savingPro.html", dataset = data, size=size)
        else :
            return render_template("/my/error_saving.html", info="적금코드 확인")


# 프로그램 시작점
if __name__ == "__main__" :
    app.run() # application 실행

