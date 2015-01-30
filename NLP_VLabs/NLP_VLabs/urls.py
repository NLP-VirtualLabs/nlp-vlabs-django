from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from NLP import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NLP_Vlabs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^register/$', views.register_page),
    url(r'^home/$', views.main_page),
    url(r'^logout/$', views.logout_page),
    url(r'^admin/', include(admin.site.urls)),

)

