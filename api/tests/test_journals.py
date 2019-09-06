import pytest

from api.tests.factories import JournalFactory


@pytest.mark.django_db
def test_journals_can_be_listed(client):
    num_items_to_list = 3
    JournalFactory.create_batch(num_items_to_list)

    response = client.get('/api/journals/')
    assert response.status_code == 200
    assert len(response.data['results']) == num_items_to_list


@pytest.mark.django_db
def test_a_single_journal_can_be_retrieved_by_id(client):
    journal = JournalFactory()
    response = client.get('/api/journals/%d/' % journal.id)
    assert response.status_code == 200
    assert response.data['id'] == journal.id


@pytest.mark.django_db
def test_a_single_journal_can_be_retrieved_by_name(client):
    name = 'test journal'
    journal = JournalFactory(name=name)
    response = client.get('/api/journals/', {'name': journal.name})
    assert response.status_code == 200
    assert response.data['results'][0]['name'] == name
