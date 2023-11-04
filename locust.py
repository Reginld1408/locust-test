import time
import random
from flask import Flask
from locust import HttpUser, task, between

# Basic Load Testing

app = Flask(__name__)
PORT = 3000


class MyUser(HttpUser):
    wait_time = between(1, 5)  # Time between requests in seconds
    
    @task
    def hello(self):
        self.client.get("/hello")

    @task
    def slow(self):
        self.client.get("/slow")

if __name__ == '__main__':
    app.run(port=PORT)
    
    
# # Auth Load Testing

# class QuickstartUser(HttpUser):
#     def __init__(self, parent):
#         super(QuickstartUser, self).__init__(parent)
#         self.token = ""

#     wait_time = between(1, 2)

#     def on_start(self):
#         with self.client.get(url="/login") as response:
#             self.token = response.json()["token"]

#     @task
#     def secret_page(self):
#         self.client.get(url="/secret", headers={"authorization": self.token})

# # Data Load Testing ( Data and Failures )

# class User(HttpUser):
#     def __init__(self, parent):
#         super(User, self).__init__(parent)
#         self.token = ""

#     wait_time = between(1, 2)

#     def on_start(self):
#         with self.client.get(url="/login") as response:
#             self.token = response.json()["token"]

#     @task
#     def user_page(self):
#         user_id = str(random.randint(0, 3))
#         self.client.get(url="/users/" + user_id,
#                         headers={"authorization": self.token},
#                         name="Users"
#                         )