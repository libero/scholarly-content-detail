import pytest

from tests.factories import CategoryFactory


@pytest.mark.parametrize('num_of_categories', [1, 3, 0])
def test_categories_can_be_listed(client, num_of_categories):
    CategoryFactory.create_batch(size=num_of_categories)
    response = client.get('/categories')

    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert len(response.json['items']) == num_of_categories


def test_get_category_by_id(client):
    category = CategoryFactory()
    response = client.get('/categories/%s' % category.id)

    assert response.status_code == 200
    assert response.content_type == 'application/json'
    expected = {
        'id': category.id,
        'name': category.name
    }
    assert response.json == expected


def test_get_category_by_id_returns_404_if_id_does_not_exist(client):
    response = client.get('/categories/1234')
    assert response.status_code ==  404
    assert response.content_type == 'application/problem+json'


def test_get_category_by_name(client):
    category = CategoryFactory()
    response = client.get('/categories?name=%s' % category.name)

    assert response.status_code == 200
    assert response.content_type == 'application/json'
    expected = {'items': [
        {
            'id': category.id,
            'name': category.name
        }
    ]}
    assert response.json == expected


def test_get_category_by_name_returns_empty_if_name_does_not_exist(client):
    response = client.get('/categories?name=test-name')

    assert response.status_code ==  200
    assert response.content_type == 'application/json'
    assert response.json == {'items': []}
