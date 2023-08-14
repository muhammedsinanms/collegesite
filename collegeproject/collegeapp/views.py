from django.contrib import auth, messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Department
from . models import Team


# Create your views here.
def home(request):
   obj = Department.objects.all()
   pic = Team.objects.all()
   return render(request,"index.html",{'result': obj, 'staff': pic})


def Form(request):
   return render(request,"form.html")



