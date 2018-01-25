# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import *


# Create your views here.
def index(request):
    user = User.objects.all()
    context ={
        'users': user
    }
    return render(request, "users.html", context)

def newForm(request):
    return render(request, 'form.html')

def process(request):
    a = User.objects.create(first_name=request.POST['first_name'],\
                                last_name=request.POST['last_name'],\
                                email=request.POST['email'])

    return redirect('/users/')

def delete(request, number):
    num = User.objects.get(id=number)
    num.delete()
    return redirect('/users')

def show(request, number):
    num = User.objects.get(id=number)
    context={
        'id':num.id,
        'first_name':num.first_name,
        'last_name':num.last_name,
        'email':num.email,
        'created_at':num.created_at
    }
    return render(request, "user_detail.html", context)

def edit(request, number):
    num = User.objects.get(id=number)
    if request.method=="POST":
        num.first_name = request.POST['first']
        num.last_name = request.POST['last']
        num.email = request.POST['email']
        num.save()
    context = {
        'id': num.id,
        'fn': num.first_name,
        'ln': num.last_name,
        'email':num.email,
    }
    return render(request,'edit.html', context )

def edited(request):
    pass
