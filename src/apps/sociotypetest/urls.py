from django.conf.urls import url

from . import views


app_name = 'sociotypetest'
urlpatterns = [
    url(r'^(?P<personal_id>[0-9]+)/$', views.sociotest, name = 'sociotest'),
    url(r'^(?P<personal_id>[0-9]+)/sociotest_result', views.sociotest_result, name = 'sociotest_result'),
]