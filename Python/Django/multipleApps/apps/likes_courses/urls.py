from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^login$', views.login),
    url(r'^users$', views.users),
    url(r'^users/new/$', views.newUser),
    url(r'^register$', views.newUser),
]
