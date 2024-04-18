from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, django. You're at the databaseManager home.")
