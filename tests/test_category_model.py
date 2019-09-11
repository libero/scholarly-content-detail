from scholarly_content_detail.models import Category
from tests import factories


def test_category_save_method(app):
    with app.app_context():
        Category(id='1').save()
        category = Category.query.get('1')
        assert category.id == '1'


def test_category_delete_method(app):
    with app.app_context():
        Category(id='1').save()
        category = Category.query.get('1')
        category.delete()

        category = Category.query.get('1')
        assert category is None


def test_a_category_can_be_saved_when_adding_articles_using_add_articles_by_id_method(app):
    with app.app_context():
        articles = factories.ArticleFactory.create_batch(size=3)
        category = Category(id='1')
        category.add_articles_by_id(article_ids=[a.id for a in articles])
        category.save()

        category = Category.query.get('1')
        assert len(category.articles) == 3


def test_category_articles_can_be_updated_when_adding_articles_using_add_articles_by_id_method(app):
    with app.app_context():
        factories.CategoryFactory(id='1', articles=1)
        category = Category.query.get('1')
        assert len(category.articles) == 1

        articles = factories.ArticleFactory.create_batch(size=2)
        category.add_articles_by_id(article_ids=[a.id for a in articles])
        category.save()

        category = Category.query.get('1')
        assert len(category.articles) == 3
