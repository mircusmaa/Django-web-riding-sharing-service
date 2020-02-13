"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from ridesharing import views as ridesharing_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',ridesharing_views.register,name='register'),
    path('register-driver/',ridesharing_views.register_driver,name='register-driver'),
    path('login/',auth_views.LoginView.as_view(template_name='ridesharing/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='ridesharing/logout.html'),name='logout'),
    path('profile/',ridesharing_views.profile,name='profile'),
    path('startride/',ridesharing_views.startride,name='startride'),
    path('driveride/',ridesharing_views.driveride,name='driveride'),
    path('join-viewride/<int:ride_id>/<int:passengers_num>/',ridesharing_views.joinviewride,name='joinviewride'),
    path('join-inforide/',ridesharing_views.joininforide,name='joininforide'),
    path('edit-ride/',ridesharing_views.edit_ride,name='edit-ride'),
    path('edit-save-ride/<int:ride_id>/',ridesharing_views.edit_save_ride,name='edit-save-ride'),
    path('view-ride/',ridesharing_views.view_ride,name='view-ride'),
    path('close-ride/',ridesharing_views.close_ride,name='close-ride'),
    path('view-confirmed-ride/',ridesharing_views.view_confirmed_ride,name='view-confirmed-ride-ride'),
    path('',include('ridesharing.urls')),
]
