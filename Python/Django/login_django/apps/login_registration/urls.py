from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^addUser$', views.addUser),
    url(r'^success$', views.successPage),
    url(r'^login$', views.loginUser),
    url(r'^$', views.index),
]
