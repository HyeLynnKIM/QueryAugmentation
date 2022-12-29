import re

## Insert 'FROM [TABLE] into SQL
def Insert_FROM(sql: str):
    ## regular expression - SQL 작성 순서대로
    p1 = re.compile('select\s.*\swhere', re.I)
    p2 = re.compile('select\s.*\sgroup by', re.I)
    p3 = re.compile('select\s.*\shaving', re.I)
    p4 = re.compile('select\s.*\sorder by', re.I)
    p5 = re.compile('select\s.*\slimit', re.I)

    # Save the front part of 'FROM'
    try: # 먼저 where 있을 때 확인
        text = str(re.match(p1, sql))
        text = text.split('match=\'')[1].split('\'')[0].split('select ')[1].split('where')[0]
        sql = re.sub(p1, 'select ' + text + 'FROM [table] where', sql)
    except:
        try: # where X -> group by 확인
            text = str(re.match(p2, sql))
            text = text.split('match=\'')[1].split('\'')[0].split('select ')[1].split('group by')[0]
            sql = re.sub(p2, 'select ' + text + 'FROM [table] where', sql)
        except:
            if re.match(p3, sql) != None: # group by X -> having 확인
                text = str(re.match(p3, sql))
                text = text.split('match=\'')[1].split('\'')[0].split('select ')[1].split('having')[0]
                sql = re.sub(p3, 'select ' + text + 'FROM [table] where', sql)
            elif re.match(p4, sql) != None: # having X -> order by 확인
                text = str(re.match(p4, sql))
                text = text.split('match=\'')[1].split('\'')[0].split('select ')[1].split('order by')[0]
                sql = re.sub(p4, 'select ' + text + 'FROM [table] where', sql)
            elif re.match(p5, sql) != None: # order by X -> limit 확인
                text = str(re.match(p5, sql))
                text = text.split('match=\'')[1].split('\'')[0].split('select ')[1].split('limit')[0]
                sql = re.sub(p5, 'select ' + text + 'FROM [table] where', sql)
            else: # select만 있는 경우 (조건 X)
                sql = sql + ' FROM [table]'

    return sql

if __name__=='__main__':
    sql = 'select avg ( matches )'
    print(Insert_FROM(sql))
