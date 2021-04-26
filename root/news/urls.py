from django.urls import path, re_path
from .views import _list, create, details, edit, delete


urlpatterns = [
    path('list', _list),
    path('create', create),
    re_path(r'^details/(?P<post_id>[0-9]+)$', details),
    re_path(r'^edit/(?P<post_id>[0-9]+)$', edit),
    re_path(r'^delete/(?P<post_id>[0-9]+)$', delete),
]