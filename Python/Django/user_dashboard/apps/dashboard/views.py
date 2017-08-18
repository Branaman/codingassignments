# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *
def specUser(request, user_id):
    userid = user_id
    userset = {"User" : User.objects.get(id=userid)}
    return render(request, "dashboard/specuser.html", userset)
def newUser(request):
    return render(request, "dashboard/newUser.html")
def processNewUser(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        return redirect('dashboard/users/new')
    else:
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        print "new User page opened"
        return redirect("dashboard/users")
def deleteUser(request, user_id):
    userid = user_id
    b = User.objects.get(id=userid)
    b.delete()
    return redirect("dashboard/users")
def editUser(request, user_id):
    userid = {"userid" :user_id}
    return render(request, "dashboard/editUser.html", userid)
def processEditUser(request):
    errors = User.objects.basic_validator(request.POST)
    user_id=request.POST['user_id']
    if len(errors):
        return redirect('dashboard/users/{}/edit'.format(user_id))
    else:
        b = User.objects.get(id=user_id)
        b.first_name=request.POST['first_name']
        b.last_name=request.POST['last_name']
        b.email=request.POST['email']
        b.updated_at=models.DateTimeField(auto_now = True)
        b.save()
        return redirect("dashboard/users/{}".format(user_id))
def users(request):
    userset = {"Users" : User.objects.all()}
    print "users page opened"
    return render(request, "dashboard/users.html", userset)
