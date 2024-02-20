import sqlite3
from flask import Flask, g

app = Flask(__name__)
cursor = g.cursor()

def getDB():
    if 'db' != g:
        g.db = sqlite3.connect("main.db")

    return g.db

def getUser(user_id):
    curs = cursor.execute(f'SELECT id FROM users WHERE id = {user_id}')
    return curs.fetchone()
    

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()