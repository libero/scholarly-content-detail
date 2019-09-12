from flask import Flask

from scholarly_content_detail.article_views import get_articles_blueprint


def create_app(config_file_name):
    app = Flask(__name__)
    app.config.from_pyfile('configs/%s' % config_file_name)

    # recommended by flask-sqlalchemy to avoid circular imports
    from scholarly_content_detail.models import db
    # connect to database
    db.init_app(app)
    # create tables
    db.create_all(app=app)

    app.register_blueprint(get_articles_blueprint())

    return app
