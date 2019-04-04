from flask import Flask
from flask_restful import Api
from config import Config
from flask import Blueprint, render_template, abort

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
app.config.from_object(Config)

from app import routes
from app.api.quiz_controller import quiz

app.register_blueprint(quiz)

# create an instance of this class flask
# name variable from python provides name of package flask uses this value to find out what's the location
# so that it can then locate other files in the same location

     