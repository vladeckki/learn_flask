from flask import Blueprint

bp = Blueprint('auth', __name__)

from flaskapp.auth import routes