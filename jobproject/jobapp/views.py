from django.http import HttpResponse
from django.shortcuts import render,redirect
jobtitle=['first job','Second Job']
jobdesc=['First job Desc', 'Second job Desc']
# Create your views here.
def hello(request):
    joblist= "<ul>"
    for j in jobtitle:
        id=(jobtitle.index(j))
        joblist+=f"<li><a href='job/{id}'>{j}</a></li>"
    joblist+="</ul>"
    return HttpResponse(joblist)


def jobs(request,id):
    if id==0:
        return redirect('/')
    returnhtml=f"<h1>{jobtitle[id]}</h1><br><h1>{jobdesc[id]}</h1>"
    return HttpResponse(returnhtml)