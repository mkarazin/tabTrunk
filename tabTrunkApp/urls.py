from django.conf.urls import patterns, url

from tabTrunkApp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^view/(?P<tab_id>\d+)/$', views.detail, name='detail'),
    url(r'^edit/(?P<tab_id>\d+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<tab_id>\d+)/$', views.delete, name='delete'),
    url(r'^new/$', views.new, name='new'),
    url(r'^create/$', views.create, name='create'),
    url(r'^register/$', views.register, name='register'),
    url(r'^changePassword/$', views.changePassword, name='changePassword')
)