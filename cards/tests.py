from django.test import TestCase
import re

class CardsTestClass(TestCase):

    def test_root_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_cards_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        self.assertRegex(response.content, re.compile(b"<h1>DE Cards Home</h1>", re.IGNORECASE))

    def test_cards_about_view(self):
        #
        # Note: URL needs a trailing '/' or we get a 301
        #
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

        self.assertRegex(response.content, re.compile(b"<h1>Put Cards About Page Here</h1>", re.IGNORECASE))
