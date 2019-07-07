from django.conf.urls import url
from . import views  # This line is new!


urlpatterns = [
    # url(r'^$', views.index, name="index")
    url(r"^new/$", views.new, name="new"),
    url(r"^create/$", views.create, name="create"),
    url(r"^login/$", views.login, name="login"),
    url(r"^logout/$", views.logout, name="logout"),
    # url(r'^show/(?P<user_id>\d+)/$', views.show, name="show"),# This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r"^edit/(?P<user_id>\d+)/$", views.edit, name="edit"),
    url(r"^update/(?P<user_id>\d+)/$", views.update, name="update"),
    # url(r'^delete/(?P<user_id>\d+)/$', views.delete, name="delete")
]
