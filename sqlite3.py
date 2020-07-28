import sqlite3 as sql

# Создание базы данных

con = sql.connect('example.db')
cur = con.cursor()

# Создание таблицы

cur.execute("""CREATE TABLE IF NOT EXISTS albums
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title text, 
                  artist text, 
                  release_date text,
                  publisher text, 
                  media_type text)""")

# Вставляем данные в таблицу

cur.execute("""INSERT INTO albums (title, artist, release_date, publisher, media_type)
                  VALUES ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3')""")

# Сохраняем изменения

con.commit()

# Вставляем множество данных в таблицу используя безопасный метод "?"

albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]

cur.executemany("INSERT INTO albums (title, artist, release_date, publisher, media_type) VALUES (?,?,?,?,?)", albums)
con.commit()

# Обновление БД

sql = """
UPDATE albums 
SET artist = 'John Doe' 
WHERE artist = 'Andy Hunter'
"""

# Удаление из БД

cur.execute(sql)
con.commit()

sql = "DELETE FROM albums WHERE artist = 'John Doe'"

cur.execute(sql)
con.commit()

sql = "SELECT * FROM albums WHERE artist=?"
cur.execute(sql, [("Red")])
print(cur.fetchall())

# Вывести таблицу отсортированную по столбцу artist

print("Here's a listing of all the records in the table:")
for row in cur.execute("SELECT rowid, * FROM albums ORDER BY artist"):
    print(row)

print("Results from a LIKE query:")
sql = "SELECT * FROM albums WHERE title LIKE 'The%'"
cur.execute(sql)

print(cur.fetchall())

# Закрыть базу
con.close()