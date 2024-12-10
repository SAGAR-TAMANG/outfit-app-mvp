from django.urls import path, re_path
from .views import index, app, suggest, profile, cart, saved

urlpatterns = [
    path('', index, name='index'),
    path('app/', app, name='app'),
    path('app/new-suggestion/', suggest),
    path('profile/', profile, name='profile'),
    path('cart/', cart, name='cart'),
    path('saved/', saved, name='saved'),

    # Matches any html file
    # re_path(r'^.*\.*', pages, name='pages'),
]