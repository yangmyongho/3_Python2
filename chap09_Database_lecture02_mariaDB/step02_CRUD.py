'''
CRUD
 - Create, Read, Update, Delete
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


try :
    # 1. db 연동 객체
    conn = pymysql.connect(**config)

    # 2. cursor 객체 : sql 문
    cursor = conn.cursor()

    # 4. Insert
    '''
    code = int(input('code :'))
    name = input('name :')
    su = int(input('su :'))
    dan = int(input('dan :'))
    sql = f"insert into goods values({code}, '{name}', {su}, {dan})"
    cursor.execute(sql)
    conn.commit()
    '''

    # 5. Update : code -> su,dan 수정
    '''
    code = int(input('수정 code :'))
    su = int(input('수정 su :'))
    dan = int(input('수정 dan :'))
    sql = f"update goods set su = {su}, dan = {dan} where code = {code}"
    cursor.execute(sql)
    conn.commit()
    '''

    # 6. Delete : code -> 유무확인 -> 삭제 or '코드없음'
    '''
    code = int(input('삭제 code :'))
    cursor.execute(f"select *from goods where code = {code}")
    row = cursor.fetchone()
    if row :
        cursor.execute(f"delete from goods where code = {code}")
        conn.commit()
    else :
        print('코드 없음')
    '''

    # 3. Read(select)
    sql = "select * from goods"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row[0], row[1], row[2], row[3])
    print('전체 레코드 수 :', len(data))
    # 상품명 조회
    '''
    name = input('조회 상품명 입력 :')
    sql = f"select * from goods where name like '%{name}%'"
    cursor.execute(sql)
    data2 = cursor.fetchall()
    if data2 :
        for row in data2:
            print(row)
    else :
        print('조회 상품 없음')
    '''
    # 상품코드 조회
    '''
    code = int(input('조회 코드 입력'))
    sql = f"select *from goods where code like {code}"
    cursor.execute(sql)
    data3 = cursor.fetchone() # 검색된 레코드 1개 반환
    if data3:
        print(data3)
    else:
        print('조회 상품 없음')
    '''

except Exception as e:
    print('db 연동 오류 :', e)
    conn.rollback()  # 이전 쿼리 실행 취소한다.
finally:
    cursor.close()
    conn.close()


















