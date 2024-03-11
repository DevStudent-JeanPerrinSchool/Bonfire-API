import sqlite3, datetime
from flask import Flask, g

#Disclaimer: all input value from a request, is a string value.

app = Flask(__name__)

def getDB():
    if 'db' != g: g.db = sqlite3.connect("main.db")

    return g.db

def getUser(user_id):
    cursor = getDB().cursor()
    if user_id.isnumeric():
        curs = cursor.execute(f'SELECT * FROM users WHERE id={user_id}')
        return curs.fetchone()
    else:
        try: curs = cursor.execute(f"SELECT * FROM users WHERE username='{user_id}'")
        except sqlite3.Error as er:
            print(f"[{datetime.datetime.now()}]: {er.sqlite_errorname} | {er} | {er.sqlite_errorcode}")
            #If there's an error, check if it's a syntax error. 
            #er converted to string because er is part of sqlite3.Error class
            if 'syntax' in str(er): return 'wrong type' 
            else: return 'error'
        #If it's not, return all user's information
        else: return curs.fetchone()

def createUser(username):
    try:
        getDB().cursor().execute(f"INSERT INTO users(username) VALUES ('{username}');")
        g.db.commit()
    except sqlite3.Error as er:
        print(f"[{datetime.datetime.now()}]: {er.sqlite_errorname} | {er} | {er.sqlite_errorcode}")
        return 'error'
    else: return 'success'

def deleteUser(user_id):
    cursor = getDB().cursor()
    if user_id.isnumeric():
        try:                
            curs = cursor.execute(f"DELETE FROM users WHERE id='{user_id}'")
            g.db.commit()
        except sqlite3.Error as er:
            print(f"[{datetime.datetime.now()}]: {er.sqlite_errorname} | {er} | {er.sqlite_errorcode}")
            if 'syntax' in str(er): return 'wrong type' 
            else: return 'error'
        else: return 'success'

def createPost(content):
    cursor = getDB().cursor()
    curs = cursor.execute(f"INSERT INTO posts (content) VALUES ('{content}');")
    curs.commit()

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)
    if db != None: db.close()