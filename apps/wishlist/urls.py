from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'create_item$', views.create_item, name='create'),
    url(r'wishlist/(?P<id>\d+)$', views.wishlist, name='wishlist'),
    url(r'add_item/(?P<id>\d+)$', views.add_item, name='add_item'),
    url(r'remove/(?P<id>\d+)$', views.remove, name='remove'),

]
