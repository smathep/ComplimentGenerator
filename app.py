from flask import Flask, render_template
import sqlite3
import datetime
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
    return render_template('index.html', compliments=compliments)

# if __name__ == "__main__":
#     app.run(host='0.0.0.0')