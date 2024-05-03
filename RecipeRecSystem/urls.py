"""
URL configuration for RecipeRecSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from pages.views import registration_view, home, logout_view

urlpatterns = [
    path("", home, name="home"),  # Home page
    path("registration/", registration_view, name="registration"),  # Registration page
    path("login/", auth_views.LoginView.as_view(), name="login"),  # Login page
    path('logout/', logout_view, name='logout'),
    path('admin/', admin.site.urls),  # Django admin
    path("", include("databaseManager.urls")),  # Include databaseManager app URLs
]

urlpatterns += staticfiles_urlpatterns()
