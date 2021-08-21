from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from blog.models import User

@receiver(post_save, sender=User)
def create_onetoone(sender, **kwargs):

    if kwargs['created']:
        from .profile_models import Profile

        Profile.objects.create(user=kwargs['instance'])