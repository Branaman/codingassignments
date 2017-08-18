from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^processBook$', views.processBook),
    url(r'^add$', views.addBook),
    url(r'^$', views.index),
]
