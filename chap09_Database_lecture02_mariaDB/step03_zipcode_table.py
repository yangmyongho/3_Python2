'''
text file -> DB 저장

<작업 순서>
    1. table 생성
    2. zipcode.txt(서울) -> readline -> 레코드 저장
    3. table 저장 -> 동으로 검색

형식)
 code   city      gu         dong           detail
135-806  서울	 강남구	개포1동 경남아파트
135-807	 서울	 강남구	개포1동 우성3차아파트	(1∼6동)
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
    # 1. db 연동 객체
    conn = pymysql.connect(**config)

    # 2. cursor 객체 : sql 문
    cursor = conn.cursor()

    # 3. table 생성
    '''
    sql = """create or replace table zipcode_tab(
    code char(14) not null,
    city char(20) not null,
    gu varchar(20) not null,
    dong varchar(80) not null,
    detail varchar(80)
    )"""
    cursor.execute(sql)
    # create는 자동으로 저장되어서 conn.commit() 생략가능
    print('1. table 작성 완료~~')
    '''

    # 4. 레코드 추가 / 조회
    sql = "select * from zipcode_tab"
    cursor.execute(sql)
    data = cursor.fetchall()
    if data: # True -> 검색

        for row in data:
            print("[%s]    %s    %s    %s    %s"%row)
        print('전체 레코드 수 :', len(data))

        # 1. 구 검색
        '''
        gu = input('검색할 구 입력 :')
        cursor.execute(f"select *from zipcode_tab where gu like '%{gu}%'")
        data2 = cursor.fetchall()
        if data2 :
            for row in data2:
                print("[%s]    %s    %s    %s    %s"%row)
        else :
            print('해당 구 없음')
        print('전체 레코드 수 :', len(data2))
        '''
        # 2. 동으로 검색
        '''
        dong = input('검색할 동 입력 :')
        cursor.execute(f"select *from zipcode_tab where dong like '%{dong}%'")
        data3 = cursor.fetchall()
        if data3:
            for row in data3:
                print("[%s]    %s    %s    %s    %s"%row)
        else :
            print('해당 동 없음')
        print('전체 레코드 수 :', len(data3))
        '''

    else: # False -> 레코드 추가
        file = open("./chap09_Database/data/zipcode.txt", encoding='utf-8')
        line = file.readline()
        while line :
            row = line.split('\t')
            if row[1] == '서울':
                code = str(row[0]) ; city = row[1] ; gu = row[2]
                dong = row[3] ; detail = row[4] # 세부주소
                if detail : # detail 이있으면
                    sql=f"""insert into zipcode_tab values(
                    '{code}','{city}','{gu}','{dong}','{detail}')"""
                else :
                    sql = f"""insert into zipcode_tab
                    (code, city, gu, dong) values(
                    '{code}','{city}','{gu}','{dong}')"""
                cursor.execute(sql)
                conn.commit()
            line = file.readline() # 다시 while 문으로 가서 반복
        file.close()
        print('2. 레코드 추가 성공~~')

except Exception as e:
    print('db 연동 오류 :', e)
    conn.rollback()  # 이전 쿼리 실행 취소한다.
finally:
    cursor.close()
    conn.close()


