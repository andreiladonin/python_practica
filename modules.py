import sqlite3
def chek(table, log, password ):

    db = sqlite3.connect("Baza.db")

    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM {table} ")

    res = cursor.fetchall()

    flag = False
    for i in res:
        if i[1] == log and i[2] == password:
            flag = True


    db.close()
    return flag

# users = chek("users", "vasya", "wtf")
# print(users)