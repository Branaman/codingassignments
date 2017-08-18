# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
def logoutUser(request):
    request.session.clear()
    return redirect('/')
def index(request):
    if "loggedIn" in request.session and request.session['loggedIn'] == True:
        return redirect("/dash")
    else:
        return render(request, "login_app/index.html")

def loginUser(request):
    result=ErrorCheck(request, "Login")
    if result['fail']:
        return redirect('/')
    else:
        return redirect("/dash")
