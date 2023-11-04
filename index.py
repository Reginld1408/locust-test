# Basic Load Testing

from flask import Flask
import time

app = Flask(__name__)
PORT = 3000

@app.route('/hello')
def hello():
    return 'Hello'

@app.route('/slow')
def slow():
    time.sleep(2)
    return 'Slow'

if __name__ == '__main__':
    app.run(port=PORT)

# # Auth Load Testing 

# from flask import Flask, request, jsonify
# import functools

# app = Flask(__name__)
# PORT = 3000

# def login_middleware(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         token = request.headers.get('Authorization')
#         if token != 'secret-token':
#             return 'Not logged in', 403
#         return func(*args, **kwargs)
#     return wrapper

# @app.route('/login', methods=['GET'])
# def login():
#     response = {
#         'token': 'secret-token'
#     }
#     return jsonify(response)

# @app.route('/secret', methods=['GET'])
# @login_middleware
# def secret():
#     return 'Welcome to the secret page'

# if __name__ == '__main__':
#     app.run(port=PORT)

# # Data Load Testing ( Data and Failures )

# from flask import Flask, request, jsonify
# import functools

# app = Flask(__name__)
# PORT = 3000

# def login_middleware(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         token = request.headers.get('Authorization')
#         if token != 'secret-token':
#             return 'Not logged in', 403
#         return func(*args, **kwargs)
#     return wrapper

# users = [
#     {"name": "Adam", "id": 0},
#     {"name": "Bob", "id": 1},
#     {"name": "Charlie", "id": 2}
# ]

# @app.route('/login', methods=['GET'])
# def login():
#     response = {
#         'token': 'secret-token'
#     }
#     return jsonify(response)

# @app.route('/users/<int:user_id>', methods=['GET'])
# @login_middleware
# def get_user(user_id):
#     user = next((user for user in users if user["id"] == user_id), None)
#     if user is None:
#         return 'No user found', 404
#     return jsonify(user)

# if __name__ == '__main__':
#     app.run(port=PORT)

