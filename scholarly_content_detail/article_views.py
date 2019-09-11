from flask import Blueprint, Response, request

from scholarly_content_detail import models


def get_articles_blueprint():
    blueprint = Blueprint('articles', __name__)

    @blueprint.route('/articles/<string:article_id>', methods=['PUT'])
    def articles(article_id):
        article = models.Article.query.get(article_id)
        status = 200
        if not article:
            article = models.Article(id=article_id)
            status = 201
        if request.json:
            category_ids = request.json.get('categories', [])
            article.categories = []
            article.add_categories_by_id(category_ids)
        article.save()
        return Response(status=status)

    return blueprint
