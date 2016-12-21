from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'create$', views.create, name='create'),
    url(r'wishlist/(?P<id>\d+)$', views.wishlist, name='wishlist'),
    url(r'add_item/(?P<id>\d+)$', views.add_item, name='add_item'),
    url(r'delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'remove/(?P<id>\d+)$', views.remove, name='remove'),
    url(r'add_wish/(?P<id>\d+)$', views.add_wish, name='add_wish'),


]
