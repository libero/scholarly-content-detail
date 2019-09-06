import pytest

from api.tests.factories import CategoryFactory


@pytest.mark.django_db
def test_categories_can_be_listed(client):
    num_items_to_list = 3
    CategoryFactory.create_batch(num_items_to_list)

    response = client.get('/api/categories/')
    assert response.status_code == 200
    assert len(response.data['results']) == num_items_to_list


@pytest.mark.django_db
def test_a_single_category_can_be_retrieved_by_id(client):
    category = CategoryFactory()
    response = client.get('/api/categories/%d/' % category.id)
    assert response.status_code == 200
    assert response.data['id'] == category.id


@pytest.mark.django_db
def test_a_single_category_can_be_retrieved_by_name(client):
    name = 'test category'
    category = CategoryFactory(name=name)
    response = client.get('/api/categories/', {'name': category.name})
    assert response.status_code == 200
    assert response.data['results'][0]['name'] == name
