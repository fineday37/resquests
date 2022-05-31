"""preview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views, search, search2, testdb

urlpatterns = [
    url(r'^hello/$', views.runoob),
    # url(r'^/$', search.search_form),
    path('testdb/', testdb.testdb),
    path('Contact/', testdb.Contacts),
    path('admin/', admin.site.urls),
    url(r'^search/$', search.search),
    url(r'search_from/$', search.search_form),
    url(r'^search-post/$', search2.search_post),
    path('name/', search.name)
]
