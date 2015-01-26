from django.conf.urls import patterns, include, url
from NLP import views

urlpatterns = patterns('',
   url(r'^login/', views.loginview, name='login')

)
