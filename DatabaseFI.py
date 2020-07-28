import sqlite3 as sql

print("1 - добавление\n2 - получение\n3 - удаление по id\n4 - очистить таблицу")
choice = int(input("> "))
con = sql.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name STRING, surname STRING)")

    if choice == 1:
        name = input("Name\n> ")
        surname = input("Surname\n> ")
        cur.execute("INSERT INTO test (name, surname) VALUES (?, ?)", (name, surname))
    elif choice == 2:
        cur.execute("SELECT * FROM test")
        rows = cur.fetchall()
        for row in rows:
            print(row[0], row[1], row[2])
    elif choice == 3:
        print("Delete id")
        delete = int(input("> "))
        cur.execute(f"DELETE FROM test WHERE id = {delete}")
    elif choice == 4:
        cur.execute("DELETE FROM test")
    else:
        print("Вы ошиблись")

    con.commit()
    cur.close()