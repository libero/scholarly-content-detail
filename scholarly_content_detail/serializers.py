from marshmallow_sqlalchemy import ModelSchema

from scholarly_content_detail import models


class BaseSchema(ModelSchema):
    class Meta:
        sqla_session = models.db.session


class CategorySerializer(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = models.Category
        fields = ('id', 'name',)


class ArticleSerializer(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = models.Article


# Instantiate Serializers
category_serializer = CategorySerializer()
article_serializer = ArticleSerializer()
