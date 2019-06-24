import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    #We  store the secret key  here in the config file
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    #We store the DB information here
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #So we do not signal the application everytime a change is made