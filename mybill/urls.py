"""mybill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

import xadmin
xadmin.ROOT_PATH_NAME = 'xadmin'
xadmin.EXPORT_MAX = 500
xadmin.DEFAULT_RELFIELD_STYLE = {'fk': 'fk_raw', 'm2m': 'm2m_raw'}
settings.XADMIN_EXCLUDE_PLUGINS = ('bookmark', 'topnav', 'themes', 'language', 'refresh', 'sortable', 'chart')
xadmin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'xadmin/', include(xadmin.site.urls)),
]
