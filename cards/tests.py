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

        #
        # test that the about.html template properly handles the page title as a parameter
        #
        self.assertRegex(response.content, re.compile(b"<title>DE Cards - About</title>", re.IGNORECASE))

        #
        # test that about.html uses the main.css file
        #
        self.assertRegex(response.content,
                re.compile(b"<link[^>]+\"/static/cards/main.css\">", re.IGNORECASE))

        #
        # test that about.html has the "Home" link
        #
        # FIXME: these sort of tests are pointless, but I'm putting them here
        #        in preparation for playing with XPath tests.
        #
        self.assertRegex(response.content, re.compile(b"<a href=\"/\">Home</a>", re.IGNORECASE))
