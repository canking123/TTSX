from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^check_user_is_repeated/$', views.check_user_is_repeat),
    url(r'^register_handle/$', views.register_handle),
    url(r'^active(?P<uid>\d+)/$', views.active),
    url(r'^login/$', views.login),
]
