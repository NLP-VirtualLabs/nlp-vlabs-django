from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NLP_VLabs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^NLP/',include('NLP.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
