import re

## Insert 'FROM [TABLE] into SQL
def Insert_FROM(sql: str):
    p = re.compile('select\s.*\swhere', re.I)

    # Save the front part of 'FROM'
    text = str(re.match(p, sql))
    text = text.split('match=\'')[1].split('\'')[0].split('select ')[1].split('where')[0]
    sql = re.sub(p, 'select '+text+'FROM [table] where', sql)

    return sql

if __name__=='__main__':
    sql = input()
    print(Insert_FROM(sql))
