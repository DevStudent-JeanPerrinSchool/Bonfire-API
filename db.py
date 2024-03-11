import sqlite3
from flask import Flask, g

app = Flask(__name__)

def getDB():
    if 'db' != g:
        g.db = sqlite3.connect("main.db")

    return g.db

def getUser(user_id):
    cursor = getDB().cursor()
    curs = cursor.execute(f"SELECT * FROM users WHERE id = {user_id};")
    return curs.fetchone()

def createUser(username):
    cursor = getDB().cursor()
    curs = cursor.execute(f"INSERT INTO users (username) VALUES ('{username}');")
    curs.commit()

def deleteUser(user_id):
    cursor = getDB().cursor()
    curs = cursor.execute(f"DELETE FROM users WHERE id = {user_id}; DELETE FROM posts WHERE user_id = {user_id}")
    curs.commit()

def createPost(content, user_id):
    cursor = getDB().cursor()
    curs = cursor.execute(f"INSERT INTO posts (content, user_id) VALUES ('{content}', {user_id});")
    curs.commit()

def deletePost(post_id):
    cursor = getDB().cursor()
    curs = cursor.execute(f"DELETE FROM posts WHERE post_id = {post_id};")
    curs.commit()

def getPost(post_id):
    cursor = getDB().cursor()
    curs = cursor.execute(f"SELECT * FROM posts WHERE post_id = {post_id};")
    return curs.fetchone()

def changeUser(user_id, username):
    cursor = getDB().cursor()
    curs = cursor.execute(f"UPDATE users SET username = '{username}' WHERE id = {user_id};")
    curs.commit()

def modifyPost(post_id, content):
    cursor = getDB().cursor()
    curs = cursor.execute(f"UPDATE posts SET content = '{content}' WHERE post_id = {post_id};")
    curs.commit()

#To Do: Show posts(user_id)

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()