import importlib

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models



try:
    # UserProfile class imported from app if python path in settings
    # py_path is dotted python path as string
    py_path = settings.DJANGO_SIMPLE_ACCOUNTS['USER_PROFILE_PYTHON_PATH']
    # get module that holds UserProfile model
    user_profile_module = importlib.import_module(py_path.rsplit('.', 1)[0])
    # get UserProfile model from module
    UserProfile = getattr(
        user_profile_module,
        py_path.rsplit('.', 1)[-1],
    )

    def create_profile(sender, instance, created, **kwargs):
        """Create a matching profile whenever a user object is created."""
        if created:
            UserProfile.objects.get_or_create(user=instance)

    models.signals.post_save.connect(create_profile, sender=User)

except KeyError as e:
    # if no UserProfile class in settings, then no UserProfile
    pass
