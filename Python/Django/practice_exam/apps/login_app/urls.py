from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^users/(\d{1,})$', views.userX),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^dash$', views.dash),
    url(r'^users$', views.users),
    url(r'^ninjagold$', views.ninjaGold),
    url(r'^mine$', views.Mine),
    url(r'^$', views.index),
]
