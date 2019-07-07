from django.conf.urls import url
from . import views

# This line is new!


urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^create/$", views.create, name="create"),
    url(r"^view/$", views.view, name="view"),
    url(r"^edit/(?P<quote_id>\d+)/$", views.edit, name="edit"),
    url(r"^update/(?P<quote_id>\d+)/$", views.update, name="update"),
    url(r"^delete/(?P<quote_id>\d+)/$", views.delete, name="delete"),
    url(r"^like/(?P<quote_id>\d+)/$", views.like, name="like"),
    url(r"^unlike/(?P<quote_id>\d+)/$", views.unlike, name="unlike"),
]

