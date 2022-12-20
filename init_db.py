import sqlite3

connection = sqlite3.connect('db/CommentGen.db')


with open('db/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

def insert_author(lname, fname):
    cur.execute("INSERT INTO authors (l_name, f_name) VALUES (?, ?)",
            (lname, fname))

def insert_compliment(lname, fname, comp):
    author = cur.execute('SELECT author_id FROM authors WHERE f_name = ? AND l_name = ?', (fname, lname)).fetchall()[0][0]
    # print(f'author_id: {author}')
    cur.execute("INSERT INTO compliments (author_id, content) VALUES (?, ?)",
            (author, comp))
# Add authors into DB
insert_author('Smathers', 'Patrick')
insert_author('Smith', 'Corinne')
insert_author('Collins', 'Katelynne')
# cur.execute("INSERT INTO authors (l_name, f_name) VALUES (?, ?)",
#             ('Smathers', 'Patrick'))
# cur.execute("INSERT INTO authors (l_name, f_name) VALUES (?, ?)",
#             ('Smith', 'Corrine'))

#Add compliments
# insert_compliment('Smathers', 'Patrick', 'The message would go here. Can be something short or a few sentences.')

insert_compliment('Smathers', 'Patrick', "Hi Alana :)\n\
            I hope you know just how sweet and amazing you are. You help so many families and kids and are making a big impact. Don't forget that")
insert_compliment('Smathers', 'Patrick', "There are a lot of days when I'm really stressed and overloaded, and simply even a simple encouraging text from you can make me feel so much better. So I hope that this message can help do the same for you <3")
insert_compliment('Smathers', 'Patrick', "Do you remember when we planned our mountain trip? We were just thinking a nice getaway to the mountains and brevard would be nice, but we had no idea that that night we would tell each other three incredible words for the first time. Truly the best day of my life <3")
insert_compliment('Smathers', 'Patrick', "I think it's so sweet and incredible that I found someone who is also so close to her family. I'm happy to find someone who also talks to their family every night and likes to visit them!")
insert_compliment('Collins', 'Katelynne', "You are such a beautiful person! I hope you see that each and every day :D")
insert_compliment('Collins', 'Katelynne', "I'm so thankful you made the group chat! You were able to unite so many people together and I'm so grateful for it!")
insert_compliment('Collins', 'Katelynne', "You are such a wonderful friend! I'm always here for you!")
insert_compliment('Collins', 'Katelynne', "I'm thankful for our memories together :D")
insert_compliment('Collins', 'Katelynne', "You are so kind and funny! You always make me smile!")
insert_compliment('Collins', 'Katelynne', "You are so hardworking and we are all proud of what you've done! Please remember to take breaks, you deserve it!")



connection.commit()
connection.close()