from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse('Hello world')
def jobs(request,id):
    return HttpResponse(f'Job Details Page {id}')