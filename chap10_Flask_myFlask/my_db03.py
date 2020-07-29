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
    sql = """create or replace table saving(
    jcode int primary key,
    jname varchar(30) not null,
    bcode int not null,
    period int not null,
    rate float not null
    )"""
    cursor.execute(sql)
    cursor.execute("insert into saving value(101, '신한인싸자유적금', 1, 1, 2.80)")
    cursor.execute("insert into saving value(102, '쏠편한작심3일적금', 1, 1, 1.70)")
    cursor.execute("insert into saving value(103, '쏠편한선물하는적금', 1, 1, 2.50)")
    cursor.execute("insert into saving value(104, '신한스마트적금', 1, 1, 1.80)")
    cursor.execute("insert into saving value(105, 'KB내맘대로적금', 2, 1, 2.25)")
    cursor.execute("insert into saving value(106, 'KB맑은하는적금', 2, 1, 2.35)")
    cursor.execute("insert into saving value(107, 'KB스마트폰적금', 2, 1, 2.40)")
    cursor.execute("insert into saving value(108, 'KB국민ONE적금', 2, 1, 2.50)")
    cursor.execute("insert into saving value(109, '금연성공적금', 3, 1, 3.00)")
    cursor.execute("insert into saving value(110, '마이트립적금', 3, 1, 1.80)")
    cursor.execute("insert into saving value(111, '내맘적금', 3, 1, 1.55)")
    cursor.execute("insert into saving value(112, '함께하는사랑적금', 3, 1, 2.10)")
    cursor.execute("insert into saving value(113, 'D-day적금', 4, 1, 2.70)")
    cursor.execute("insert into saving value(114, 'W소확행통장', 4, 1, 3.30)")
    cursor.execute("insert into saving value(115, '나이야가라통장', 4, 1, 1.95)")
    cursor.execute("insert into saving value(116, 'W효도적금', 4, 1, 1.60)")
    cursor.execute("insert into saving value(117, 'WON모아적금', 5, 1, 3.50)")
    cursor.execute("insert into saving value(118, 'L.point적금', 5, 1, 2.50)")
    cursor.execute("insert into saving value(119, 'WON적금', 5, 1, 2.00)")
    cursor.execute("insert into saving value(120, '우리프렌즈적금', 5, 1, 2.20)")
    cursor.execute("insert into saving value(121, '올원5늘도적금', 6, 1, 1.35)")
    cursor.execute("insert into saving value(122, '법사랑플러스적금', 6, 1, 1.90)")
    cursor.execute("insert into saving value(123, 'NH성공파트너적금', 6, 1, 1.91)")
    cursor.execute("insert into saving value(124, 'NH20해봄적금', 6, 1, 1.85)")
    cursor.execute("insert into saving value(125, '정기적금', 7, 1, 1.05)")
    cursor.execute("insert into saving value(126, 'JB여행스토리적금', 7, 1, 1.05)")
    cursor.execute("insert into saving value(127, 'JB행복결혼적금', 7, 1, 1.10)")
    cursor.execute("insert into saving value(128, 'JB행복드림적금', 7, 1, 1.15)")
    cursor.execute("insert into saving value(129, '원더풀산타적금', 8, 1, 1.30)")
    cursor.execute("insert into saving value(130, '원더풀라이프적금', 8, 1, 2.00)")
    cursor.execute("insert into saving value(131, '참행복한적금', 8, 1, 1.00)")
    conn.commit()


    sql = "select *from saving"
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
