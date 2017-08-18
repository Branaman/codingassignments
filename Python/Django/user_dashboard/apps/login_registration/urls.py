from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^addUser$', views.addUser),
    url(r'^success$', views.successPage),
    url(r'^processlogin$', views.loginUser),
    url(r'^login$', views.loginPage),
    url(r'^register$', views.registerPage),
    url(r'^$', views.index),
]
