from app import app
from app.model import User, Post, db

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
