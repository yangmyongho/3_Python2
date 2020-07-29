''''
table 전체 조회 -> 생성 및 조회
 1. table 없는경우 : table 생성
 2. table 있는경우 : table 조회
'''
import pymysql
config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}


try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # 1. 전체 table 조회
    cursor.execute("show tables")
    tables = cursor.fetchall()
    # table 유무 검색
    sw = False # 스위칭 기법
    if tables:
        for t in tables:
            #print(t) # tuple 타입  ('emp_table',)
            #print(t[0]) # table 이름만  emp_table
            if t[0] == 'emp': # 찾을 테이블 이름 입력
                sw = True
    if sw == False: # table 생성 -> 레코드 삽입
        #print('emp 테이블 없음')
        sql = """create table emp(
        eno int auto_increment primary key,
        ename varchar(20) not null,
        hiredate date not null,
        sal int,
        bonus int default 0,
        job varchar(20) not null,
        dno int
        )"""
        cursor.execute(sql) # table 생성

        sql2 = "alter table emp auto_increment = 1001"
        cursor.execute(sql2)

        sql3 = """insert into emp(ename, hiredate, sal, bonus, job, dno)
        values('홍길동', '2010-10-20', 300, 35, '관리자', 10)"""
        cursor.execute(sql3)
        sql3 = """insert into emp(ename, hiredate, sal, bonus, job, dno)
        values('이순신', '2015-09-20', 250, 15, '사원', 20)"""
        cursor.execute(sql3)
        sql3 = """insert into emp(ename, hiredate, sal, job, dno)
        values('유관순', '2020-08-20', 220, '사원', 10)"""
        cursor.execute(sql3)
        conn.commit()
        print('emp 테이블 작성 완료~~')

    else: # 레코드 조회
        #print('emp 테이블 있음')
        sql = "select *from emp"
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            print(row)
        print('전체 레코드 수 :', len(data))

        # 사원 조회 : 키보드(이름) -> 사번,이름,부서 출력 or '해당사원 없음'
        '''
        name = input('조회할 사원의 이름 :')
        cursor.execute(f"select * from emp where ename like '%{name}%'")
        data2 = cursor.fetchall()
        if data2 :
            for row in data2:
                print(row)
            print('전체 레코드 수 :', len(data2))
        else:
            print('해당사원 없음')
        '''
        # 사원 수정 : 키보드(사번, 급여, 보너스) -> 급여,보너스 수정
        '''
        eno = int(input('수정 사번 :'))
        sal = int(input('수정 급여 :'))
        bonus = int(input('수정 보너스 :'))
        sql = f"update emp set sal={sal}, bonus={bonus} where eno={eno}"
        cursor.execute(sql)
        conn.commit()
        cursor.execute(f"select *from emp where eno={eno}")
        row = cursor.fetchall()
        print(row)
        '''
        # 레코드 삭제 : 키보드(사번) -> 검색(유무) -> 레코드 삭제 or '없음'
        '''
        eno = int(input('삭제할 사원번호 :'))
        cursor.execute(f"select *from emp where eno = {eno}")
        data = cursor.fetchall()
        if data:
            cursor.execute(f"delete from emp where eno = {eno}")
            conn.commit()
            cursor.execute(f"select *from emp")
            row = cursor.fetchall()
            print(eno, '삭제')
        else :
            print('해당 사원 없음')
        '''

except Exception as e:
    print('db 연동 오류 :', e)
    conn.rollback()  # 이전 쿼리 실행 취소한다.
finally:
    cursor.close()
    conn.close()





























































