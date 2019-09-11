import pytest

from scholarly_content_detail import models
from tests import factories
from tests.factories import CategoryFactory


def test_an_article_can_be_created_by_put_request_without_categories(app, client):
    with app.app_context():
        response = client.put('/articles/1')
        assert response.status_code == 201

        article = models.Article.query.get('1')
        assert len(article.categories) == 0


@pytest.mark.parametrize('num_of_cats', [0, 1, 5])
def test_an_articles_can_be_created_by_put_request_with_categories(app, client, num_of_cats):
    with app.app_context():
        categories = CategoryFactory.create_batch(size=num_of_cats)
        response = client.put(
            '/articles/%d' % num_of_cats,
            json={'categories': [c.id for c in categories]}
        )
        assert response.status_code == 201

        article = models.Article.query.get('%d' % num_of_cats)
        assert len(article.categories) == num_of_cats


def test_existing_article_categories_are_replaced_by_put_request_with_categories(app, client):
    with app.app_context():
        article = factories.ArticleFactory(id='1', categories=2)
        categories = factories.CategoryFactory.create_batch(2)
        assert [c.id for c in article.categories] != [c.id for c in categories]

        response = client.put(
            '/articles/1',
            json={'categories': [c.id for c in categories]}
        )
        assert response.status_code == 200

        article = models.Article.query.get('1')
        assert [c.id for c in article.categories] == [c.id for c in categories]
