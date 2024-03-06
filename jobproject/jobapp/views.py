from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render,redirect
from django.urls import reverse
from django.template import loader
jobtitle=['first job','Second Job','Third Job']
jobdesc=['First job Desc', 'Second job Desc','Third job Desc']
# Create your views here.
"""def hello(request):
    joblist= "<ul>"
    for j in jobtitle:
        id=(jobtitle.index(j))
        jd=reverse("jobdet",args=(id,))
        joblist+=f"<li><a href='{jd}'>{j}</a></li>"
    joblist+="</ul>"
    return HttpResponse(joblist)"""

def hello(request):
    template=loader.get_template('hello.html')
    context={'name':"Arneeth"}
    return HttpResponse(template.render(context,request))


def jobs(request,id):
    try:
        if id==0:
            return redirect(reverse('jobhome'))
        returnhtml=f"<h1>{jobtitle[id]}</h1><br><h1>{jobdesc[id]}</h1>"
        return HttpResponse(returnhtml)
    except:
        return HttpResponseNotFound('Not Found')