from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Deck(models.Model):
    deck_name = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
