"""config URL Configuration

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
from django.urls import path, include
from main import views as main_views
from fkuki2019 import views as fkuki2019_views
from django.contrib.auth import views as auth_views
from main.forms import UserLoginForm
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('akun/', include('django.contrib.auth.urls')),
    path('akun/login', auth_views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name='login'),
    path('', main_views.index, name='index'),
    path('profil/', main_views.profil, name='profil'),
    path('cari/', main_views.cari, name='cari'),
    path('materi/', fkuki2019_views.materi, name='materi'),
    path('materi/<slug:slug>/', fkuki2019_views.materi_detail, name='materi_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
