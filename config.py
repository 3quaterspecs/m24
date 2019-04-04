import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # if there is an environment variable called secret key, get the value from that.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # if it signals the application whenever an object change
    SQLALCHEMY_TRACK_MODIFICATIONS = False