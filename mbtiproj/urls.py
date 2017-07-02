"""mbtiproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'rootproj'
urlpatterns = [
    url(r'', include('src.apps.registration.urls'), name = 'registration'),
    url(r'^personalp/', include('src.apps.personalp.urls'), name = 'personalp'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^sociotypetest/', include('src.apps.sociotypetest.urls'), name = 'sociotypetest'),
    #url(r'^registration/', include('src.apps.registration.urls'), name = 'registration'),
    url(r'^authentification/', include('src.apps.authentification.urls'), name = 'authentification'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL)