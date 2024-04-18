from django.urls import path

from databaseManager import views

urlpatterns = [
    path('', views.home, name='home'),
]