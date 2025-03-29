from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Meeting
from django.urls import reverse_lazy
from .forms import MeetingForm
from django.urls import path

 # Create your views here.
def index(request):
    meetings= Meeting.objects.all()
    info = {'meetings': meetings}
    return render(request, 'meetingbook/index.html', info)

def addmeeting(request):
    info ={}
    form = MeetingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
        
    info['form']= form
    return render(request, "meetingbook/addmeeting.html", info)


def meetingdetails(request, id):
    info ={}
    info["data"] = Meeting.objects.get(id = id)
    return render(request, "meetingbook/meetingdetails.html", info)

def updatemeeting(request, id):
    info ={}
    obj = get_object_or_404(Meeting, id = id)
    form = MeetingForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('index')
    info["form"] = form
    return render(request, "meetingbook/updatemeeting.html", info)
    
    
def deletemeeting(request, id):
    Meeting.objects.get(id=id).delete()
    return redirect('index')