from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    response = HttpResponse()
    response.write('<h1>Welcome!</h1>')
    response.write('<h2><u>This is my first Django application</u></h2>')
    return response