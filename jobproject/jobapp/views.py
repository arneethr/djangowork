from django.http import HttpResponse
from django.shortcuts import render
jobtitle=['first job','Second Job']
jobdesc=['First job Desc', 'Second job Desc']
# Create your views here.
def hello(request):
    return HttpResponse('Hello world')
def jobs(request,id):
    id=int(id)-1
    returnhtml=f"<h1>{jobtitle[id]}</h1><br><h1>{jobdesc[id]}</h1>"
    return HttpResponse(returnhtml)