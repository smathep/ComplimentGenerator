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
    cur.execute("INSERT INTO compliments (author_id, content) VALUES (?, ?)", (author, comp))
    # cur.execute('INSERT INTO view_count')

# Add authors into DB
# insert_author('Smathers', 'Patrick')
# insert_author('Smith', 'Corinne')
# insert_author('Collins', 'Katelynne')
# insert_author('Pagilagan', 'Karl')
# insert_author('Taylor', 'Caden')
# insert_author('Dad', 'Your')
# insert_author('Mom', "Your")
# insert_author('Smathers', 'Isabel')
# insert_author('Mom', 'My')
# insert_author('Kissoon', 'Kevin')
# insert_author('Kissoon', 'Sheranie')
# insert_author('McGuire', 'Brendan')
# insert_author('Payne', 'Jordan')
# insert_author('Chen', 'Stephen')


#Add compliments
# insert_compliment('Smathers', 'Patrick', 'The message would go here. Can be something short or a few sentences.')
#Already Added
# insert_compliment('Smathers', 'Patrick', "Hi Alana :)\nI hope you know just how sweet and amazing you are. You help so many families and kids and are making a big impact. Don't forget that")
# insert_compliment('Smathers', 'Patrick', "There are a lot of days when I'm really stressed and overloaded, and simply even a simple encouraging text from you can make me feel so much better. So I hope that this message can help do the same for you <3")
# insert_compliment('Smathers', 'Patrick', "Do you remember when we planned our mountain trip? We were just thinking a nice getaway to the mountains and brevard would be nice, but we had no idea that that night we would tell each other three incredible words for the first time. Truly the best day of my life <3")
# insert_compliment('Smathers', 'Patrick', "I think it's so sweet and incredible that I found someone who is also so close to her family. I'm happy to find someone who also talks to their family every night and likes to visit them!")
# insert_compliment('Collins', 'Katelynne', "You are such a beautiful person! I hope you see that each and every day :D")
# insert_compliment('Collins', 'Katelynne', "I'm so thankful you made the group chat! You were able to unite so many people together and I'm so grateful for it!")
# insert_compliment('Collins', 'Katelynne', "You are such a wonderful friend! I'm always here for you!")
# insert_compliment('Collins', 'Katelynne', "I'm thankful for our memories together :D")
# insert_compliment('Collins', 'Katelynne', "You are so kind and funny! You always make me smile!")
# insert_compliment('Collins', 'Katelynne', "You are so hardworking and we are all proud of what you've done! Please remember to take breaks, you deserve it!")
# insert_compliment('Pagilagan', 'Karl', "If you ever need anything we're a call away :)")
# insert_compliment('Pagilagan', 'Karl', "You know if things get kinda tough, we could always hang out to relieve some stress 👀 You, patty, and I could go for another din din night 👀👀")
# insert_compliment('Pagilagan', 'Karl', "I couldn't really think of another inspirational quote, so instead here's a quote from Yoko Ono that I think you'd like. \"AAAAHHHhahHahahahHhuuhhHWHOoooooOooOoOoOoOooOoo\"")
# insert_compliment('Taylor', 'Caden', "Thanks for seeing something in me at the protest! Now I've never been more grateful to have such a wonderful friend!")
# insert_compliment('Taylor', 'Caden', "Who could ask for a better person to be queen of the Clemson Friends")
# insert_compliment('Taylor', 'Caden', "I wanna make a joke about Freud but my ego is getting the best of me")
# insert_compliment('Dad', 'Your', "You think you're having a bad day? Well, I'm sitting in a room without any view trying to look through a hole in the sky! Okay, well I guess I shouldn't complain because the rent's never due, but God knows as Robert's dog knows, all day long I think of things, but nothing seems to satisfy. Am I going insane, or what?!\nYou know,\n\"One thing you can't hide - is when you're crippled inside.\"\n But always keep in mind,\n\"All you need is love.\"\nAnd certainly,\n\"Don't carry the world upon your shoulders.\"\nYou know, no one's perfect. But,\n\"With every mistake, we must surely be learning.\"\nAlana, if you're having a big disagreement with someone close to you remember,\n\"Life is very short and there's no time for fussing and fighting my friend.\"\nAnd no matter what, always remember:\n\"The long and winding road that leads to home will never disappear.\"\n\"Take my advice: If you're feeling lazy and don't want to think of good quotes, use Google.\" - Dad")
# insert_compliment('Mom', 'Your', "Remember that you are doing so much good in the children's lives. You are making a big difference. Think about how thankful and appreciative some of the parents have been for your help; suggestions and support. All the cute kids you get to play with and the progress they are making with your help.\n\n Remember how flexible this job is and you don't have anyone micro managing you and all the time spent working at Panera instead of working behind a boring desk.\n\nRemember how good it felt when you helped that sweet kid to use the potty.\n\nDo not put so much pressure on yourself for not making the goal for the month, as your supervisor is not making it a huge deal. You don't know if others are in the same boat. Remember all the good things your supervisor said to you about how good a job you are doing. They need you and the kids need you.\n\nWork on developing a \"thick skin\" and not let things people say bother you as it has in the past. See it as, you know yourself better than they do or take things as constructive criticism.\n\nFind time to drink water because it is important and will help you feel better. \n\nI am proud of you and love you very much!\n\nMom")
# insert_compliment('Smathers', 'Isabel', "Hello")
# insert_compliment('Mom', 'My', "Dear Alana, for the not so good days just remember how far you have come and rememeber all the people that love you. And we are proud of you")
# insert_compliment('Smith', 'Corinne', "Ours is the friendship I want to last forever")
# insert_compliment('Smith', 'Corinne', "Never forget you won Biggest Glow Up for a reason")
# insert_compliment('Smith', 'Corinne', "Your capacity to care for others is something I've always admired")
# insert_compliment('Smith', 'Corinne', "You look like Dora ('s age-appropriate, hotter older sister)")
# insert_compliment('Smith', 'Corinne', "What you are doing now is important, even if you're not treated like it")
# insert_compliment('Smith', 'Corinne', "Live. Laugh. Love. ✨.")
# insert_compliment('Smith', 'Corinne', "You will always be my Simran")
# insert_compliment('Smith', 'Corinne', "You are not the fourth letter word")
# insert_compliment('Smith', 'Corinne', "Hunter probably counts you in his top 10 regrets ")
# insert_compliment('Smith', 'Corinne', "I truly couldn't ask for a best friend, I love you!")
# insert_compliment('Kissoon', 'Sheranie', "Hi Alana!! hope everything is well with you. I want you to know I am extremely proud of the woman you have become. I've always thought of you as my little sister and I adore all the moments we have spent together. Your smile and laugh fills up the room! No matter where Kevin and I are in this world, just know that you can always reach out to us if you need anything. You hold a special place in our hearts. We love you a lot! -Sheranie")
# insert_compliment('Kissoon', 'Kevin', "Alana, I am so proud of you, and watching you become this strong woman right in front of my eyes has become a true blessing.\n You help the future of so many children and that alone is one of the most important jobs of our time.  I love you and can’t wait to write some more on this amazing website - Kevin Kissoon")
# insert_compliment('McGuire', 'Brendan', "You seem like such a great person, I'm so excited to finally meet you in person!")
# insert_compliment('Payne', 'Jordan', "You're cooler than pat")
#To add
# insert_compliment('Chen', 'Stephen', "Breathe. It's just a bad day, not a bad life.\n\nJust remember how hard you pushed yourself today and that tomorrow will be a better day. Keep pushing on Alana, proud of ya!")

connection.commit()
connection.close()
