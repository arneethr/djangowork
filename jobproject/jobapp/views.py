from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render,redirect
from django.urls import reverse
from django.template import loader
jobtitle=['no','first job','Second Job','Third Job']
jobdesc=['no','First job Desc', 'Second job Desc','Third job Desc']
# Create your views here.
def joblist(request):
    vals={'joblist':jobtitle}
    return render(request,'jobapp/joblist.html',vals)

def hello(request):  
    auth=True
    context={'name':"Arneeth", 'auth':auth}
    return render(request,'jobapp/hello.html',context)


def jobs(request,id):
    try:
        if id==0:
            return redirect(reverse('jobhome'))
        dic={'id':id,'jobtitle':jobtitle[id],'jobdesc':jobdesc[id]}
        return render(request,'jobapp/jobs.html',dic)
    except:
        return HttpResponseNotFound('Not Found')