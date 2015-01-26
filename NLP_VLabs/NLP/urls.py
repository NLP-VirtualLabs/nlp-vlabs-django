from django.conf.urls import patterns, include, url
from NLP import views

urlpatterns = patterns('',
   url(r'^login/', views.loginview, name='login')
   url(r'^auth/', views.auth_and_login, name='auth_and_login'),
   url(r'^signup/', views.sign_up_in, name='sign_up_in'),

)
