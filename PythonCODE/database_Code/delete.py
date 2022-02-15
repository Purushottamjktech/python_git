import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        apple = sqlite3.connect('firstTable.db')
        return apple
    except Error:
        print(Error)


def sql_table(apple):
    cursorObj = apple.cursor()
    cursorObj.execute("SELECT * FROM employee")
    rows = cursorObj.fetchall()
    print(" details:")
    for row in rows:
        print(row)

    s_id = 1003
    cursorObj.execute("""
    DELETE FROM employee WHERE employee_id = ?
    """,(s_id, ))
## we can also do this wy
    # cursorObj.execute("""
    #    DELETE FROM employee WHERE employee_id = 1002
    #    """)
    apple.commit()


    cursorObj.execute("SELECT * FROM employee")
    rows = cursorObj.fetchall()
    print("\n")
    print("Table after deletion operation is performed\n")
    for row in rows:
        print(row)


sqllite_apple = sql_connection()
sql_table(sqllite_apple)
if sqllite_apple:
    sqllite_apple.close()
    print("\n exit here")
