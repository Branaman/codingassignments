from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^users/(\d{1,})$', views.specUser),
    url(r'^$', views.users),
    url(r'^users/new$', views.newUser),
    url(r'^adduser$', views.processNewUser),
    url(r'^users/(\d{1,})/edit$', views.editUser),
    url(r'^users/(\d{1,})/delete$', views.deleteUser),
    url(r'^processedit$', views.processEditUser),
]
