"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include, url
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.signIn),
    url(r'^postsign/',views.postsign),
    url(r'^logout/',views.logout,name="log"),
    url(r'^signup/',views.signUp,name='signup'),
    url(r'^postsignup/',views.postsignup,name='postsignup'),
    url(r'^create/',views.create,name='create'),
    url(r'^post_create/',views.post_create,name='post_create'),
    url(r'^check/',views.check,name='check',
    url(r'^post_check/',view.post_check,name='post_check'),
]
