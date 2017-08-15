from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^addCourse$', views.addCourse),
    url(r'^courses/destroy/(\d{1,})$', views.confDelCourse),
    url(r'^delCourse$', views.delCourse),
    url(r'^$', views.coursesIndex),
]
