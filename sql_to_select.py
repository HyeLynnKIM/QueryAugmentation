import re
from updat_FROM import *

def Change_SQL_space(sql: str):
    # max - min 의 형태인 경우 처리
    p = re.compile('select\smax.*\s-\smin\s.*', re.I)
    if re.match(p, sql) != None:
        sql = sql.replace(' - ', ' , ')
        return sql
    
    # count, sum, avg 경우 처리
    if 'count ( ' or 'sum ( ' or 'avg ( ' in sql:
        conf = 'count'
        if 'sum ( ' in sql:
            conf = 'sum'
        elif 'avg ( ' in sql:
            conf = 'avg'

        head = sql.split(f'{conf} ( ')[0] # select
        item = sql.split(f'{conf} ( ')[1].split(' )')[0] # count 안 item

        if item == '': item = '*' # ex: select count (  ) where report = '97-81' 같이 괄호 빈 경우
        tail = sql.split(f'{conf} ( ')[1].split(' )')[1] # 뒷부분
        sql = head + item + tail

    return sql

def Change_SQL_CAP(sql: str):
    # max - min 의 형태인 경우 처리
    p = re.compile('SELECT\sMAX.*\s-\sMIN.*', re.I)
    if re.match(p, sql) != None:
        sql = sql.replace(' - ', ' , ')
        return sql

    # MAX 만 뽑는 경우 처리

    # count, sum, avg 경우 처리
    conf = ''
    if 'COUNT(' in sql:
        conf = 'COUNT'
    elif 'SUM(' in sql:
        conf = 'SUM'
    elif 'AVG(' in sql:
        conf = 'AVG'

    if conf != '':
        head = sql.split(f'{conf}(')[0]  # select
        item = sql.split(f'{conf}(')[1].split(')')[0]  # count 안 item

        if item == '': item = '*'  # ex: select count (  ) where report = '97-81' 같이 괄호 빈 경우
        tail = sql.split(f'{conf}(')[1].split(')')[1]  # 뒷부분
        sql = head + item + tail

    return sql

if __name__=='__main__':
    sql = 'select avg ( matches )' # example
    sql = Insert_FROM(sql)
    print(Change_SQL_space(sql))
