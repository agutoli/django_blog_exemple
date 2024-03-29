from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^blog/?$', 'agutoli.blog.views.index', name='home_url_name'),
    url(r'^blog/(?P<post_id>\d+)','agutoli.blog.views.detail'),
    url(r'^admin/?', include(admin.site.urls)),

    # url(r'^agutoli/', include('agutoli.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #defaul index
    url(r'', 'agutoli.blog.views.index'),
)
