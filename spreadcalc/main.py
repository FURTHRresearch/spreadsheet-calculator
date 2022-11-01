import flask

from .auth import check_key

bp = flask.Blueprint('main', __name__)


@bp.route('/')
def hello():
    return 'Hello, World!'


@bp.route('/protected')
@check_key
def protected():
    return 'Hello, Protected World!'
