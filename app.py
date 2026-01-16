from flask import Flask, render_template
import sqlite3
import random
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('db/CommentGen.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def main():
    conn = get_db_connection()
    compliments = conn.execute('SELECT * FROM compliments JOIN authors USING (author_id)').fetchall()
    conn.close()
    # print(compliments[random.randrange(1,len(compliments))]['content'])
    rand_comp = compliments[random.randrange(0,len(compliments))]
    # Idea: select all quotes with a view_count of 0 and when the comment is viewed, increment it so it won't be shown until all others are shown. Once all are viewed, reset view_count
    increase_view_count(rand_comp['id'])
    # print("type: %s",type(rand_comp))
    return render_template('index.html', compliment=rand_comp)

def increase_view_count(comp_id):
    conn = get_db_connection()
    print(type(comp_id))
    # view_count = int(conn.execute('SELECT view_count FROM compliments WHERE id = ?', (comp_id,)).fetchall()[0]['view_count'])+1
    conn.execute('UPDATE compliments SET view_count = ((SELECT view_count FROM compliments WHERE id = ?)+1) WHERE id = ?', (comp_id, comp_id))
    # conn.execute('UPDATE compliments SET view_count = ?', [view_count+1])
    conn.commit()
    conn.close()

# if __name__ == "__main__":
#     app.run(host='0.0.0.0') 