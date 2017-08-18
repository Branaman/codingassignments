from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^addUser$', views.addUser),
    url(r'^login$', views.loginUser),
    url(r'^logout$', views.logoutUser),
    url(r'^$', views.index),
]
