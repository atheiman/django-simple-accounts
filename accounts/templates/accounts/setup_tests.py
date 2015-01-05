from .models import User

try:
    # if there is a UserProfile model to extend django.contrib.auth.models.User
    from .models import UserProfile

    # create a test user
    user = User(
        username = 'jtest',
        first_name = 'Joe',
        last_name = 'Test',
        email = 'jtest@gmail.com',
    )
    user.set_password('joepass')
    user.save()

except ImportError as e:
    # there is no specified UserProfile model
    pass
