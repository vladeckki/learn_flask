from flask import Blueprint

bp = Blueprint('errors', __name__)

from flaskapp.errors import handlers