from django.test import TestCase
import re

class CardsTestClass(TestCase):

    def test_root_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def test_cards_home_view(self):
        response = self.client.get('/cards/')
        self.assertEqual(response.status_code, 200)

        self.assertRegex(response.content, re.compile(b"<h1>DE Cards Home</h1>", re.IGNORECASE))
