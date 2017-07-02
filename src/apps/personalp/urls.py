from django.conf.urls import url
from . import views

app_name = 'personalp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<personal_id>[0-9]+)/$', views.personal_info, name = 'personal_info'),
]