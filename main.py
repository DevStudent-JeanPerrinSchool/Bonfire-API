from db import *
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/') #return multiple endpoints possible
def hello_world():
    return """<h1>Welcome to Bonfire API</h1>
              <p>Nothing is here... but you can try those:</p>
              <code>GET/DELETE http://localhost:5000/api/user/'user_id'</code>
              <code>POST http://localhost:5000/api/user/create</code>
              <code>GET/DELETE http://localhost:5000/api/post/'post_id'</code>"""

@app.route('/api/user/<int:user_id>', methods=['GET', 'DELETE'])
def user_methods(user_id):
    if request.method == 'GET':
        result = getUser(user_id)
        print(result)
        if result == None:
            abort(404, f'{user_id} was not found')
        else:
            return {
                "id": "",
                "username": "",
                "following": "",
                "followed_by": "",
                "created_at": ""
            }
    elif request.method == 'DELETE':
        #function to remove user from the db
        return f"user {user_id} succesfuly deleted", 200

#@app.route('/api/user/create', methods=['POST'])
#def create_new_user():

@app.route('/api/post/<int:post_id>', methods=['GET', 'DELETE'])
def post_methods(post_id):
    if request.method == 'GET': 
        #check if post_id exist catch error or return post info in json format
        return
    elif request.method == 'DELETE':
        #function to remove post from the db
        return f"post {post_id} succesfuly deleted", 200