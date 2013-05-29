from django.conf.urls import patterns, include, url

# Admin
from django.contrib import admin
admin.autodiscover()

# Users
from django.contrib.auth.views import login, logout


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tabTrunkApp.views.index'	, name='index'),
    # url(r'^$', 'TabTrunk.views.home', name='home'),
    # url(r'^TabTrunk/', include('TabTrunk.foo.urls')),
    url(r'^tabs/', include('tabTrunkApp.urls')),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
    
    # Users
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
)
