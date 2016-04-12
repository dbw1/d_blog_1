from django.conf.urls import url
from posts import views

urlpatterns = [
    url(r'^$', views.posts_list),  #appname.views.fn_name
    url(r'^create/$', views.posts_create),
    url(r'^(?P<id>\d+)/$', views.posts_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', views.posts_update, name='update'),
    url(r'^delete/$', views.posts_delete),
]
