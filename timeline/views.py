
# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{})

def get_result(request):
    return HttpResponse("recieved query: " + request.GET['query'])

# def index(request):
# 	return HttpResponse("Hello, world. You're at the polls index.")
