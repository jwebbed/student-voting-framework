from django.db import models
from django.contrib.auth.models import User

class Voter(models.Model):
    token = models.OneToOneField(User)
    voted = models.BooleanField(default=False)