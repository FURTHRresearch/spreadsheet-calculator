import flask


def create_app():
    app = flask.Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py', silent=True)

    from . import main
    app.register_blueprint(main.bp)

    return app
