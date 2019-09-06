import factory

from api import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Sequence(lambda n: "Category %d" % n)


class JournalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Journal

    name = factory.Sequence(lambda n: "Journal %d" % n)