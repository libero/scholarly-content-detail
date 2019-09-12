from scholarly_content_detail.models import Article
from tests import factories


def test_an_article_can_be_saved_when_adding_categories_using_add_categories_by_id_method(db):
    categories = factories.CategoryFactory.create_batch(size=3)
    article = Article(id='1')
    article.add_categories_by_id(category_ids=[c.id for c in categories])
    db.session.add(article)
    db.session.commit()

    article = Article.query.get('1')
    assert len(article.categories) == len(categories)


def test_article_categories_can_be_updated_when_adding_categories_using_add_categories_by_id_method(db):
    factories.ArticleFactory(id='1', categories=1)
    article = Article.query.get('1')
    assert len(article.categories) == 1

    categories = factories.CategoryFactory.create_batch(size=2)
    article.add_categories_by_id(category_ids=[c.id for c in categories])
    db.session.add(article)
    db.session.commit()

    article = Article.query.get('1')
    assert len(article.categories) == 3
