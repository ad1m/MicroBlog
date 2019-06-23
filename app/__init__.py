'''
This  script creates the application object  as an instance of  class Flask
'''

from flask import Flask

app = Flask(__name__)

from app import routes