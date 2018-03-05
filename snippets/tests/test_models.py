from django.test import TestCase
from ..models import Snippet
from django.contrib.auth.models import User


class SnippetTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        self.user = User.objects.create_user(
            id=1,username='jacob', email='jacob@…', password='top_secret')

        Snippet.objects.create(
            id=1,
            created='2018-01-04T18:09:36.612Z',
            title='serializers.py',
            code='test code field',
            linenos=False,
            language='python',
            style='default',
            owner=self.user,
            highlighted='test highlighted field'
            )


    def test_string_representation(self):
        snip = Snippet.objects.get(id=1)
        self.assertEqual(str(snip), snip.title)
