'''
sqlite3
 - 내장형 DBMS : 기기 내부에서만 사용
 - 외부 접근 허용 안됨
'''
import sqlite3
print(sqlite3.sqlite_version_info) # (3, 31, 1)



try:
    # 1. database & db연동객체  생성 < 최초에는 생성이지만 존재한다면 불러온다 >
    conn = sqlite3.connect('./chap09_Database/data/sqlite.db') # sqlite.db
    cursor = conn.cursor()# sql문 실행 객체

    # 2. table 생성
    sql = """ create table if not exists test_tab(
    name text(10),phone text(15), address text(50)) """
    cursor.execute(sql) # table 생성 <auto commit>이기떄문에 생략함

    # 3. 레코드 추가 <바깥에는 ""사용해야함> <한번추가하면끝>
    '''
    cursor.execute("insert into test_tab values('홍길동', '010-1111-1111', '서울시')")
    cursor.execute("insert into test_tab values('이순신', '010-2222-2222', '해남시')")
    cursor.execute("insert into test_tab values('유관순', '010-3333-3333', '충남시')")
    conn.commit() # db에 반영한다. 
    '''

    # 4. 레코드 조회
    cursor.execute("select *from test_tab")
    dataset = cursor.fetchall() # 객체레코드 -> 레코드 가져오기
    for row in dataset :
        print(row) # tuple타입
    print("이름\t\t\t전화번호\t\t주소")
    for row in dataset:
        print(row[0]+'\t'+row[1]+'\t'+row[2]) # 개별적 컬럼 타입

except Exception as e:
    print('db 연동 오류 :', e)
    conn.rollback() # 이전 쿼리 실행 취소한다.
finally:
    cursor.close()
    conn.close()

''' ('홍길동', '010-1111-1111', '서울시')
    ('이순신', '010-2222-2222', '해남시')
    ('유관순', '010-3333-3333', '충남시')
    이름			전화번호		주소
    홍길동	010-1111-1111	서울시
    이순신	010-2222-2222	해남시
    유관순	010-3333-3333	충남시 '''




























































