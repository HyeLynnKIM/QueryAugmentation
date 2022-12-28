import re
## Insert 'FROM [TABLE] into SQL
def Insert_FROM(sql: str):
    p = re.compile('select\s.*\swhere', re.I)

    # Save the front part of 'FROM'
    text = str(re.match(p, sql))
    text = text.split('match=\'')[1].split('\'')[0].split('select ')[1].split('where')[0]
    sql = re.sub(p, 'select '+text+'FROM [table] where', sql)

    return sql

## Insert 'FROM [TABLE] into SQL
def Change_SQL(sql: str):
    if 'count' in sql:
        head = sql.split('count ( ')[0] # select
        item = sql.split('count ( ')[1].split(' )')[0] # count 안 item
        tail = sql.split('count ( ')[1].split(' )')[1] # 뒷부분
        sql = head + item + tail

    return sql

if __name__=='__main__':
    sql = 'select count ( * ) where prize money (usd) = \'$0\'' # example
    sql = Insert_FROM(sql)
    print(Change_SQL(sql))
