from .models import *
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    Profile.objects.create(user=instance.id)
