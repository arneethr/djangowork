from django.http import HttpResponse
from django.shortcuts import render,redirect
jobtitle=['first job','Second Job']
jobdesc=['First job Desc', 'Second job Desc']
# Create your views here.
def hello(request):
    return HttpResponse('Hello world')
def jobs(request,id):
    if id==0:
        return redirect('/')
    returnhtml=f"<h1>{jobtitle[id-1]}</h1><br><h1>{jobdesc[id-1]}</h1>"
    return HttpResponse(returnhtml)