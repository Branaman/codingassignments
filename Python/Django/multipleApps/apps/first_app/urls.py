from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(\d{1,})$', views.numPage),
    url(r'^(\d{1,})/edit$', views.editPage),
    url(r'^(\d{1,})/delete$', views.delPage),
]
# /blogs - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'.
# /blogs/new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'.
# /blogs/create - Have this be handled by a method named 'create'.  For now, have this url redirect to /blogs.
# /blogs/{{number}} - display 'placeholder to display blog {{number}}.  For example /blogs/15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'.
# /blogs/{{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'.
# /blogs/{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /blogs.
