from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.core.signals import setting_changed
from django.dispatch import receiver

class CustomUser(AbstractUser):
    pass

@receiver(setting_changed)
def update_user_profile(sender, setting, value, **kwargs):
    if setting == 'AUTH_USER_MODEL':
        return None
    return True

def post_save_receiver(sender, instance, created, **kwargs):
    print('Added a user')
post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)
