# Django Simple Accounts



## Stop rewriting User views and templates!

Use these views and templates to interact with the `django.contrib.auth.models.User` model. Allow your end users to easily login, logout, register, and manage their profile.

These views and templates are designed to be bear bones, not a lot of bells and whistles here.

Don't get bogged down managing Users, focus on writing your application!



## Configuration

First, you must add the Django app `accounts` to `INSTALLED_APPS` in your settings file.

Configuration for django-simple-accounts is set in the `django.settings.DJANGO_SIMPLE_ACCOUNTS` object. None of the keys are required to be set, however **you must at least define the object with no keys** (`DJANGO_SIMPLE_ACCOUNTS = {}`).

Example configuration object with all keys set:

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



## Features to be added

- User Profile Model management

- Login with Google or Facebook

- Register

