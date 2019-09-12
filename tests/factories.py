import factory

from scholarly_content_detail import models


class CategoryFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.Category
        sqlalchemy_session = models.db.session

    id = factory.Sequence(lambda n: "%d" % n)
    name = factory.Sequence(lambda n: "Category %d" % n)

    @factory.post_generation
    def articles(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            if isinstance(extracted, int):
                extracted = ArticleFactory.create_batch(size=extracted)
            self.articles.extend(extracted)


class ArticleFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.Article
        sqlalchemy_session = models.db.session

    id = factory.Sequence(lambda n: "%d" % n)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            if isinstance(extracted, int):
                extracted = CategoryFactory.create_batch(size=extracted)
            self.categories.extend(extracted)
