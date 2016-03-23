from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def get_result(request):
    return HttpResponse("recieved query: " + request.GET['query'])
