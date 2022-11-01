import flask

from .auth import check_key

bp = flask.Blueprint('main', __name__)


@bp.route('/')
def hello():
    return 'Hello, World!'


@bp.route('/evaluate')
@check_key
def evaluate():
    return 'Hello, Protected World!'
