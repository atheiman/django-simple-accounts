import importlib

from django.conf import settings
from django.db import models



UserProfile = None

if settings.DJANGO_SIMPLE_ACCOUNTS['USER_PROFILE_PYTHON_PATH']:
    user_profile_module = settings.DJANGO_SIMPLE_ACCOUNTS['USER_PROFILE_PYTHON_PATH'].rsplit('.', 1)[0]
    user_profile_module = importlib.import_module(user_profile_module)
    UserProfile = getattr(
        user_profile_module,
        settings.DJANGO_SIMPLE_ACCOUNTS['USER_PROFILE_PYTHON_PATH'].rsplit('.', 1)[-1]
    )

if UserProfile is None:
    # create a default UserProfile
    class UserProfile(models.Model):
        age = models.PositiveSmallIntegerField()
