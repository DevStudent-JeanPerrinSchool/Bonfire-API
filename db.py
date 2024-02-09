import sqlite3
from flask import Flask, g

app = Flask(__name__)

def getDB():
    if 'db' is not g:
        g.db = sqlite3.connect("main.db")

    return g.db

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()