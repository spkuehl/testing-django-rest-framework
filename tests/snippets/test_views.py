import pytest
from django.urls import reverse
from django.conf import settings
from rest_framework.test import APIClient, APIRequestFactory
from snippets.models import Snippet
from django.contrib.auth.models import User


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


@pytest.mark.django_db
def test_api_create_snippet(client):
    client = APIClient()
    user = User.objects.create_user('john',
                                    'lennon@thebeatles.com', 'johnpassword')
    client.login(username='john', password='johnpassword')
    request = client.post('/snippets/',{
        "url": "",
        "id": 1,
        "highlight": "",
        "owner": "john",
        "title": "rolling knolls",
        "code": "123123k",
        "linenos": 'true',
        "language": "abap",
        "style": "abap"
        }, format='json')
    assert Snippet.objects.count() == 1
