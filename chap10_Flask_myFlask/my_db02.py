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
    sql = """create or replace table deposit(
    ycode int primary key,
    yname varchar(30) not null,
    bcode int not null,
    period int not null,
    rate float not null
    )"""
    cursor.execute(sql)
    cursor.execute("insert into deposit value(11, '쏠편한정기예금', 1, 1, 1.35)")
    cursor.execute("insert into deposit value(12, 'KBstar정기예금', 2, 1, 1.16)")
    cursor.execute("insert into deposit value(13, '국민첫재태크예금', 2, 1, 1.15)")
    cursor.execute("insert into deposit value(14, '하나원큐정기예금', 3, 1, 1.00)")
    cursor.execute("insert into deposit value(15, 'N플러스정기예금', 3, 1, 1.15)")
    cursor.execute("insert into deposit value(16, '1석7조정기예금', 4, 1, 1.20)")
    cursor.execute("insert into deposit value(17, 'i-ONE1000예금', 4, 1, 1.26)")
    cursor.execute("insert into deposit value(18, '우리정기예금', 5, 1, 0.75)")
    cursor.execute("insert into deposit value(19, '키위정기예금', 5, 1, 1.00)")
    cursor.execute("insert into deposit value(20, '자유로정기예금', 6, 1, 0.95)")
    cursor.execute("insert into deposit value(21, 'NH왈츠회전예금', 6, 1, 1.23)")
    cursor.execute("insert into deposit value(22, '스마트 정기예금', 7, 1, 1.10)")
    cursor.execute("insert into deposit value(23, 'JB정기예금', 7, 1, 0.60)")
    cursor.execute("insert into deposit value(24, '프리스타일예금', 8, 1, 1.20)")

    conn.commit()


    sql = "select *from deposit"
    cursor.execute(sql)
    dataset = cursor.fetchall()
    for row in dataset:
        print(row[0], row[1], row[2], row[3], row[4])
    print('전체 레코드 수 :', len(dataset))


except Exception as e:
    print('오류 :',e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
