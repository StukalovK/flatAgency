from django.urls import path, re_path
from .views import offer_list, create, details, delete, add_district, district_list, delete_district

urlpatterns = [
    path('', offer_list),
    path('offer-list', offer_list),
    path('create', create),
    re_path(r'^details/(?P<offer_id>[0-9]+)$', details),
    #re_path(r'^edit/(?P<offer_id>[0-9]+)$', edit),
    re_path(r'^delete/(?P<offer_id>[0-9]+)$', delete),
    path('district-list', district_list),
    path('add-district', add_district),
    re_path(r'^delete-district/(?P<district_id>[0-9]+)$', delete_district),
]