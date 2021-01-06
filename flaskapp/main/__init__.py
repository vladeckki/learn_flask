
from flask import Blueprint

bp = Blueprint('main', __name__)

from flaskapp.main import routes