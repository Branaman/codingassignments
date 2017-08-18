# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from ..users_app.models import ErrorCheck
from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
def logoutUser(request):
    request.session.clear()
    return redirect('/')
def index(request):
    if "loggedIn" in request.session and request.session['loggedIn'] == True:
        return redirect("/books")
    else:
        return render(request, "login_app/index.html")
def addUser(request):
    result=ErrorCheck(request, "Register")
    if result['fail']:
        return redirect('/')
    else:
        User.objects.Create(request, result)
        return redirect('/')
def loginUser(request):
    result=ErrorCheck(request, "Login")
    if result['fail']:
        return redirect('/')
    else:
        sessionUpdate(request)
        return redirect("/books")
