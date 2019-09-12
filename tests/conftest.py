import pytest

from scholarly_content_detail import create_app, models


@pytest.fixture()
def app():
    app = create_app('test.py')
    return app


@pytest.fixture
def context(app):
    """
    Adds an application context during tests. During runtime this is handled by
    the flask runner. More information can be found here:
    https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/
    """
    with app.app_context():
        yield


@pytest.fixture
def client(app, context):
    return app.test_client()


@pytest.fixture
def db(context):
    return models.db
