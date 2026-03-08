from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from pages.views import registration_view

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', registration_view, name='registration'),
    path('recipes/', views.browse_recipes, name='browse_recipes'),
    path('my-recipes/', views.my_recipes, name='my_recipes'),
]