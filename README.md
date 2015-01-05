# Django Simple Accounts



## Stop rewriting User views and templates!

Use these views and templates to interact with the `django.contrib.auth.models.User` model. Allow your end users to easily login, logout, register, and manage their profile.

These views and templates are designed to be bear bones, not a lot of bells and whistles here.

Don't get bogged down managing Users, focus on writing your application!



## Start using django-simple-accounts

1.  Install django-simple-accounts from GitHub using pip:

    `pip install git+ssh://git@github.com/atheiman/django-simple-accounts.git@master`

1.  Add the Django app `accounts` to `INSTALLED_APPS` in your settings file:

    ```python
    # settings.py

    INSTALLED_APPS = (
       # ...
       'accounts',
    )
    ```

1.  Include the django-simple-accounts urls in your `ROOT_URLCONF`:

    ```python
    # urls.py

    urlpatterns = patterns('',
        # ...
        url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    )
    ```

1.  Create your UserProfile model if desired:

    ```python
    # models.py

    class UserProfile(models.Model):
        user = models.OneToOneField(User)
        phone = models.CharField(
            max_length=12,
            blank=True,
        )
        # more model fields as needed

        def __unicode__(self):
            return self.user.username
    ```

1.  Configure django-simple-accounts in your settings:

    ```python
    # settings.py

    DJANGO_SIMPLE_ACCOUNTS = {
        # python
        'USER_PROFILE_PYTHON_PATH': 'my_app.models.UserProfile',
    }
    ```

    Configuration is described completely below.

1.  Run the app and check it out:

    ```shell
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
    ```

    You should see Profiles as a [StackedInline](https://docs.djangoproject.com/en/1.7/ref/contrib/admin/#django.contrib.admin.StackedInline) included in your admin site at [/admin/auth/user/](http://localhost:8000/admin/auth/user/).

    The following URLs / views are also implemented for use:

    - [/accounts/register/](http://localhost:8000/accounts/register/)

    - [/accounts/login/](http://localhost:8000/accounts/login/)

    - [/accounts/profile/](http://localhost:8000/accounts/profile/)

    - [/accounts/logout/](http://localhost:8000/accounts/logout/)



## Configuration

Configuration for django-simple-accounts is set in the `django.settings.DJANGO_SIMPLE_ACCOUNTS` dict. None of the keys are required to be set, however **you must at least define the dict with no keys** (`DJANGO_SIMPLE_ACCOUNTS = {}`).

Example configuration dict with all keys set:

```python
# settings.py

DJANGO_SIMPLE_ACCOUNTS = {
    'USER_PROFILE_PYTHON_PATH': 'my_app.models.UserProfile',
}
```

An explanation of each key availble to be set is described below:

### `USER_PROFILE_PYTHON_PATH`

#### Example: `'my_app.models.UserProfile'`
Dotted python path to a subclass of `django.db.models.Model` that you have defined as a User Profile model as described in the [Django docs](https://docs.djangoproject.com/en/1.7/topics/auth/customizing/#extending-the-existing-user-model). This setting allows:

- an instance of the UserProfile model is created when a new User is created
- the profile view includes fields for the UserProfile model

#### Notes:

- Be sure to set [Field.default](https://docs.djangoproject.com/en/1.7/ref/models/fields/#default) or [Field.blank](https://docs.djangoproject.com/en/1.7/ref/models/fields/#blank) and [Field.null](https://docs.djangoproject.com/en/1.7/ref/models/fields/#null) for all of your UserProfile model fields, because when the UserProfile instance is first created no fields will be set. Those fields are set from the profile view (after registration).



## A note on URLs

As recommended above, it generally makes sense to include `accounts.urls` at `/accounts/. If you are going to place these at a different location, be sure to change the LOGIN_REDIRECT_URL, LOGIN_URL, and LOGOUT_URL described [here](https://docs.djangoproject.com/en/1.7/ref/settings/#login-redirect-url).



## Features to be added

[ ] User Profile Model management

[ ] Login with Google or Facebook

[ ] Register

[ ] Email registration confirmation link

[x] Configure with django settings
