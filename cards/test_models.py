from django.test import TestCase
from .models import Card

class CardModelTest(TestCase):

    def test_string_representation(self):
        card = Card(front="the car")
        self.assertEqual(str(card), card.front)
