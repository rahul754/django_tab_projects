from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import logging
logr = logging.getLogger(__name__)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    likes_cheese = models.BooleanField()
    favourite_hamster_name = models.CharField(max_length=50)
    
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


