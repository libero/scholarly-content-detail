from flask import Flask
from flask_ping import get_ping_blueprint
from werkzeug.exceptions import HTTPException

from scholarly_content_detail.views.article_views import get_articles_blueprint
from scholarly_content_detail.views.category_views import get_categories_blueprint
from scholarly_content_detail.error_handlers import http_error_handler


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
    app.register_blueprint(get_categories_blueprint())
    app.register_blueprint(get_ping_blueprint())

    app.register_error_handler(HTTPException, http_error_handler)

    return app
