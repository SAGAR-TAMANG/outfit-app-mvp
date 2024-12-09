from django.urls import path, re_path
from .views import index, app

urlpatterns = [
    path('', index, name='index'),
    path('app/', app, name='app'),

    # Matches any html file
    # re_path(r'^.*\.*', pages, name='pages'),
]
