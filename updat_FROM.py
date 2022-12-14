import re

## Insert 'FROM [TABLE] into SQL
def Insert_FROM(sql: str):
    p = re.compile('select\s[a-zA-Z0-9]*\s', re.I)

    # Save the front part of 'FROM'
    text = str(re.match(p, sql))
    text = text.split('match=\'')[1].split('\'')[0]
    sql = re.sub(p, text+'FROM [table] ', sql)

    return sql

if __name__=='__main__':
    sql = input()
    print(Insert_FROM(sql))
