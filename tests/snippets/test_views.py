import pytest
from django.urls import reverse
from django.conf import settings


@pytest.mark.django_db
def test_fetch_users_returns_emply_list(client):
    """ Make sure that we get valid JSON response if we have no users created """
    response = client.get(reverse('user-list'))
    data = response.json()
    assert 0 == len(data["results"])


@pytest.mark.django_db
def test_fetch_snippets_returns_emply_list(client):
    """ Make sure that we get valid JSON response if we have no snippets created """
    response = client.get(reverse('snippet-list'))
    data = response.json()
    assert 0 == len(data["results"])
