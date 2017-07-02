from django.conf.urls import url
from . import views

app_name = 'authentification'
urlpatterns = [
    url(r'^login/$', views.login_for_user, name='login_for_user'),
    url(r'^logout/$', views.logout_for_user, name='logout_for_user'),
]
