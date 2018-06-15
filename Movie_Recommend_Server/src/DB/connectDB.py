import cx_Oracle

def exec():
    connstr = "scott/tiger@localhost:1521/xe"
    db = cx_Oracle.connect(connstr)
    cursor = db.cursor()
    return cursor