import sqlite3
from flask import Flask, g

app = Flask(__name__)

def getDB():
    if 'db' != g:
        g.db = sqlite3.connect("main.db")

    return g.db

def getUser(user_id):
    cursor = getDB().cursor()
    curs = cursor.execute(f'SELECT * FROM users WHERE id = {user_id}')
    return curs.fetchone()

def createUser(username):
    cursor = getDB().cursor()
    curs = cursor.execute(f"INSERT INTO users (username) VALUES ('{username}');")
    curs.commit()

def deleteUser(user_id):
    cursor = getDB().cursor()
    curs = cursor.execute(f"DELETE FROM users WHERE id = '{user_id}';")
    curs.commit()

def createPost(content):
    cursor = getDB().cursor()
    curs = cursor.execute(f"INSERT INTO posts (content) VALUES ('{content}');")
    curs.commit()

def deletePost(post_id):
    cursor = getDB().cursor()
    curs = cursor.execute(f"DELETE FROM posts WHERE post_id = '{post_id}';")
    curs.commit()

def getPost(post_id):
    cursor = getDB().cursor()
    curs = cursor.execute(f'SELECT * FROM posts WHERE post_id = {post_id}')
    return curs.fetchone()

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()