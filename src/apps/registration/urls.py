from django.conf.urls import url
from . import views

app_name = 'registration'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registration/new_account$', views.register, name='register'),
    #url(r'^login/$', 'django.contrib.auth.views.login', { "template_name": "accounts/login.html" } ),
    #url(r'^registration/logout/$', 'django.contrib.auth.views.logout_then_login' ),
]