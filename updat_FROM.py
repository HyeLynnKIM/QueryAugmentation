import re

def Insert_FROM(sql: str):
    p = re.compile(
        'select\s[a-zA-Z0-9]*\s', re.I)
    first = str(re.match(p, sql))
    first = first.split('match=\'')[1].split('\'')[0]
    sql = re.sub(p, first+'FROM [table] ', sql)

    return sql

if __name__=='__main__':
    sql = input()
    print(Insert_FROM(sql))
