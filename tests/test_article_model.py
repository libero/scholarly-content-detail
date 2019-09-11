from scholarly_content_detail.models import Article
from tests import factories


def test_article_save_method(app):
    with app.app_context():
        Article(id='1').save()
        article = Article.query.get('1')
        assert article.id == '1'


def test_article_delete_method(app):
    with app.app_context():
        Article(id='1').save()
        article = Article.query.get('1')
        article.delete()

        article = Article.query.get('1')
        assert article is None


def test_an_article_can_be_saved_when_adding_categories_using_add_categories_by_id_method(app):
    with app.app_context():
        categories = factories.CategoryFactory.create_batch(size=3)
        article = Article(id='1')
        article.add_categories_by_id(category_ids=[c.id for c in categories])
        article.save()

        article = Article.query.get('1')
        assert len(article.categories) == len(categories)


def test_article_categories_can_be_updated_when_adding_categories_using_add_categories_by_id_method(app):
    with app.app_context():
        factories.ArticleFactory(id='1', categories=1)
        article = Article.query.get('1')
        assert len(article.categories) == 1

        categories = factories.CategoryFactory.create_batch(size=2)
        article.add_categories_by_id(category_ids=[c.id for c in categories])
        article.save()

        article = Article.query.get('1')
        assert len(article.categories) == 3
