from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

try:
    # if there is a UserProfile model to extend django.contrib.auth.models.User
    from .models import UserProfile

    class UserProfileInline(admin.StackedInline):
        model = UserProfile
        can_delete = False
        verbose_name_plural = "Profile"

    # unregister the default User admin
    admin.site.unregister(User)

    # define a new User admin
    class UserAdmin(UserAdmin):
        inlines = (UserProfileInline, )

    # register the new User admin
    admin.site.register(User, UserAdmin)

except ImportError as e:
    # there is no specified UserProfile model, keep using the default User admin
    pass
