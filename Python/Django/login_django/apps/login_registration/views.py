# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
def addUser(request):
    errors = User.objects.reg_validator(request.POST)
    if request.POST['password']!=request.POST['confirm_pass']:
        errors["confirm"] = "Passwords do not match"
    if len(errors):
        for error in errors.itervalues():
            messages.add_message(request, messages.ERROR, error)
        return render(request, "login_registration/index.html")
    else:
        charliefoxtrot = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email= request.POST['email'], password=charliefoxtrot)
        errors = {'success': "Registrations successful!"}
        for error in errors.itervalues():
            messages.add_message(request, messages.ERROR, error)
        return render(request, "login_registration/index.html")
def successPage(request):
    return render(request, "login_registration/success.html")
def loginUser(request):
    errors = User.objects.login_validator(request.POST)
    print errors
    if len(errors):
        return redirect('/', errors)
    else:
        userset = {'User':User.objects.get(email=request.POST['email']).first_name}
        print userset
        return render(request, "login_registration/success.html", userset)
def index(request):
    return render(request, "login_registration/index.html")
# Create your views here.
