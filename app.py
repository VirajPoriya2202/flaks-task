from flask import Flask
app = Flask(__name__)

# @app.route("/")
# def welcome():
#     return "hello world"

# import controller.user_controller as user_controller,

from controller import *

print("hello")