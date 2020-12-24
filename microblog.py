from flaskapp import app, create_app
from flaskapp.model import User, Post, db
from flaskapp import cli


app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


