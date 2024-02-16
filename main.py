from db import *
from flask import Flask

app = Flask(__name__)

@app.route("/") #return multiple endpoints possible
def hello_world():
    return """<h1>Welcome to Bonfire API</h1>
              <p>Nothing is here... but you can try those:</p>"""

@app.route("/api/users/<userid>")
def show_user_info():
    #try search userid in DB, catch error or return "all" informations about this id in json format
    return "Nothing here..."

@app.route("/api/users/<userid>/<post_id>")
def show_post_info():
    #try search userid in DB, if doesn't exist: return => user not found (maybe go futher ? like banned or tempban ?) 
    #If user found, check if post_id exist catch error or return post info in json format
    return "Nothing here..."