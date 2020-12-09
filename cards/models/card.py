from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from .deck import Deck

class Card(models.Model):
    front = models.CharField(max_length=100)
    back = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.front

    def get_absolute_url(self):
        return reverse('card-detail', kwargs={'pk': self.pk})
