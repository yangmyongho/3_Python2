'''
group by 집단변수(범주형)
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

    # 1.부서  ,  2.직책
    gcol = int(input('1.부서  ,  2.직책  : '))
    if gcol > 2 or gcol < 1 :
        print('그룹 불가')
    else:
        if gcol == 1: # dno 그룹
            sql = """select dno, sum(sal), round(avg(sal),2) from emp 
            group by dno
            order by dno """
        elif gcol ==2: # job 그룹
            sql = """select job, sum(sal), round(avg(sal),2) from emp 
                    group by job
                    order by job """
        cursor.execute(sql)
        data = cursor.fetchall()
        group = "부서" if gcol == 1 else "직책"
        print(group, " 급여합계", " 급여평균")
        for row in data:
            print(row[0], '\t', row[1], '\t', row[2])
        print('전체 레코드 수 :', len(data))


except Exception as e:
    print('db 연동 오류 :', e)
    conn.rollback()  # 이전 쿼리 실행 취소한다.
finally:
    cursor.close()
    conn.close()


















