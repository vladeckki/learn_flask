from flask import render_template
from flaskapp import app, db
from . import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/error_404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/error_500.html'), 500