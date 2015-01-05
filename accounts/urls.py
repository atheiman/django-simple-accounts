from django.conf.urls import patterns, url

from .views import custom_login, register, profile, logout_view

urlpatterns = patterns('',
    # /login
    url(
        r'^login/$',
        custom_login,
        name='login',
    ),

    # /logout
    url(
        r'^logout/$',
        logout_view,
        name='logout',
    ),

    # /register
    url(
        r'^register/$',
        register,
        name='register',
    ),

    # /profile
    url(
        r'^profile/$',
        profile,
        name='profile',
    ),
)
