'''


'''
import pymysql
print(pymysql.version_info) # (1, 3, 12, 'final', 0)
config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}



try :
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    sql = "create or replace table bank(bcode int primary key,bname varchar(30) not null,bjoin varchar(20) not null)"
    cursor.execute(sql)

    cursor.execute("insert into bank value(1, '신한은행', 'YES')")
    cursor.execute("insert into bank value(2, '국민은행', 'YES')")
    cursor.execute("insert into bank value(3, '하나은행', 'YES')")
    cursor.execute("insert into bank value(4, '기업은행', 'YES')")
    cursor.execute("insert into bank value(5, '우리은행', 'NO')")
    cursor.execute("insert into bank value(6, '농협은행', 'NO')")
    cursor.execute("insert into bank value(7, '전북은행', 'NO')")
    cursor.execute("insert into bank value(8, '씨티은행', 'NO')")
    conn.commit()


    sql = "select *from bank"
    cursor.execute(sql)
    dataset = cursor.fetchall()
    for row in dataset:
        print(row[0], row[1], row[2])
    print('전체 레코드 수 :', len(dataset))


except Exception as e:
    print('오류 :',e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()

