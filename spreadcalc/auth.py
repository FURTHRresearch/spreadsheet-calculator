from functools import wraps

import flask


def check_key(f):
    @wraps(f)
    def decorated(*args, **kws):
        if not (flask.current_app.config['ACCESS_KEY'] == flask.request.headers.get('ACCESS-KEY')):
            flask.abort(401)
        return f(*args, **kws)
    return decorated
