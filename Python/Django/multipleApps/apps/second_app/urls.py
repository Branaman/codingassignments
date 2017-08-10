from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.surveys),
    url(r'^new$', views.addSurvey),
    ]
