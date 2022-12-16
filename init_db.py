import sqlite3

connection = sqlite3.connect('db/CommentGen.db')


with open('db/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO authors (l_name, f_name) VALUES (?, ?)",
            ('Smathers', 'Patrick'))

cur.execute("INSERT INTO compliments (author_id, content) VALUES (?, ?)",
            (1, "This is a test"))

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('First Post', 'Content for the first post')
#             )

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
#             )

connection.commit()
connection.close()