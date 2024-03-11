from db import *
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/') #return multiple endpoints possible
def hello_world():
    return """<h1>Welcome to Bonfire API</h1>
    <p>Nothing is here... but you can try those:</p>
    <code>GET/DELETE http://localhost:5000/api/user/'user_id'</code><br/>
    <code>POST http://localhost:5000/api/user/register</code><br/>
    <code>GET/DELETE http://localhost:5000/api/post/'post_id'</code>"""

#All abort() function return a HTTP Code, but also a HTML Body (bad?)

@app.route('/api/user/<user_id>', methods=['GET', 'DELETE'])
def user_methods(user_id):
    match request.method:
        case 'GET':
            result = getUser(user_id)
            match result:
                case 'error': abort(500) 
                case None: return f"User {user_id} Not Found", 404
                case 'wrong type': abort(400)
                case _: return {
                    "id": result[0],
                    "username": result[1],
                    "following": result[2],
                    "followed_by": result[3],
                    "created_at": result[5]
                }

        case 'DELETE':
            result = deleteUser(user_id)
            match result:
                case 'success': return f"User {user_id} Succesfuly Deleted", 200
                case 'error': abort(500)
                case 'wrong type': abort(400)
                    #TODO:
                    # return "need a user id to delete". I'm not putting both function as getUser 
                    # because can already have user id with getUser function.

@app.route('/api/user/register', methods=['POST'])
def create_new_user():
    if request.method == 'POST':
        dataIn = request.json
        print(dataIn)
        result = createUser(dataIn["username"])
        if result == 'success': return "User Succesfuly Created", 201
        #TODO: futher explanation on error 500
        elif result == 'error': return "Could Not Create User", 500 

#@app.route('/api/user/login', methods=['GET'])

"""
@app.route('/api/post/<int:post_id>', methods=['GET', 'POST', 'DELETE'])
def post_methods(post_id):
    match request.method:
        case 'GET': return #TODO: check if post_id exist catch error or return post info in json format
        case 'POST': return #TODO: Modify content of post
        case 'DELETE': return f"post {post_id} succesfuly deleted", 200 #TODO: remove post from the db
"""
"""
@app.route('/api/post/', methods=['GET', 'POST'])
def post_methods():
    match request.method:
        case 'GET': return #TODO: return a number of post like, 5 maybe? only with id, then use GET post to have content, text etc
        case 'POST': return #TODO: Create post
"""