"""blogging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ourblog import views as ourblog_views
from ourblog import models

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', ourblog_views.home, name="home"),
    url(r"blog/(\d+)/$", ourblog_views.blog, name="individual_blog"),
    url(r"create_blog/$", ourblog_views.create_blog, name="create_blog"),
    url(r"create_blogger/$", ourblog_views.create_blogger, name="create_blogger"),
    url(r"like/(\d+)/$", ourblog_views.like_blog, name="like_blog"),
    url(r"add_comment/(\d+)/", ourblog_views.add_comment, name="add_comment"),

    #account logins
    url(r"^account/login/$", ourblog_views.login, name="login"),
    url(r"^account/auth$", ourblog_views.auth_view, name="auth_view"),
    url(r"^account/logout/$", ourblog_views.logout, name="logout"),
    url(r"^account/loggedin/$", ourblog_views.loggedin, name="loggedin"),
    url(r"^account/invalid/$", ourblog_views.invalid_login, name="invalid_login"),
    #Acoount registrations
    url(r"^account/register/$", ourblog_views.register_user, name="register_user"),
    url(r"^account/register_success/$", ourblog_views.register_success, name="register_success"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
