from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def home(request):
    html = '<h1>Mitesh</h1>'
    return HttpResponse(html)