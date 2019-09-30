import json

from flask import Blueprint, Response, request
from werkzeug.exceptions import NotFound

from scholarly_content_detail import models
from scholarly_content_detail.serializers import category_serializer


def get_categories_blueprint():
    blueprint = Blueprint('categories', __name__)

    @blueprint.route('/categories/<string:category_id>', methods=['GET'])
    def category(category_id):
        category = models.Category.query.get(category_id)
        if category:
            return Response(
                status=200,
                content_type='application/json',
                response=category_serializer.dumps(category)
            )
        raise NotFound()

    @blueprint.route('/categories', methods=['GET'])
    def categories():
        name = request.args.get('name')
        if name:
            query = models.Category.query.filter_by(name=name)
        else:
            query = models.Category.query

        categories = query.order_by(models.Category.name.asc()).all()
        return Response(
            status=200,
            content_type='application/json',
            response=json.dumps({'items': category_serializer.dump(categories, many=True)})
        )

    return blueprint
