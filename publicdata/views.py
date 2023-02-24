from django.shortcuts import render
from django.http import HttpResponse
from .api import api

# Create your views here.


def test(request):
    return HttpResponse(api())
