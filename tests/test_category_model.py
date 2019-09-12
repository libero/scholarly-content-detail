from scholarly_content_detail.models import Category
from tests import factories


def test_a_category_can_be_saved_when_adding_articles_using_add_articles_by_id_method(db):
    articles = factories.ArticleFactory.create_batch(size=3)
    category = Category(id='1')
    category.add_articles_by_id(article_ids=[a.id for a in articles])
    db.session.add(category)
    db.session.commit()

    category = Category.query.get('1')
    assert len(category.articles) == 3


def test_category_articles_can_be_updated_when_adding_articles_using_add_articles_by_id_method(db):
    factories.CategoryFactory(id='1', articles=1)
    category = Category.query.get('1')
    assert len(category.articles) == 1

    articles = factories.ArticleFactory.create_batch(size=2)
    category.add_articles_by_id(article_ids=[a.id for a in articles])
    db.session.add(category)
    db.session.commit()

    category = Category.query.get('1')
    assert len(category.articles) == 3
