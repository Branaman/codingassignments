from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^results$', views.submitter),
    url(r'^checkout$', views.checkout),
    # url(r'^create$', views.create),
    # url(r'^(\d{1,})$', views.numPage),
    # url(r'^(\d{1,})/edit$', views.editPage),
    # url(r'^(\d{1,})/delete$', views.delPage),
]
