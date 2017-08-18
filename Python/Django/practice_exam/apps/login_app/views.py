# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect

def index(request):
    if "logged_in" in request.session:
        return redirect("/dash")
    return render(request, "login_app/index.html")
def register(request):
    results = User.objects.ErrorCheck(request, "Register")
    if results['pass']:
        User.objects.createUser(request)
        return redirect("/dash")
    else:
        return redirect("/")
def login(request):
    results = User.objects.ErrorCheck(request, "Login")
    if results['pass']:
        sessionUpdate(request)
        return redirect("/dash")
    else:
        return redirect("/")
def logout(request):
    request.session.clear()
    return redirect('/')
def dash(request):
    if "logged_in" not in request.session:
        return redirect("/")
    topFive = {"Users" : User.objects.all().order_by('-gold')[:5]}
    return render(request, "login_app/dash.html", topFive)
def users(request):
    if "logged_in" not in request.session:
        return redirect("/")
    users = {"Users": User.objects.all()}
    return render(request, "login_app/users.html", users)
def userX(request, user_id):
    if "logged_in" not in request.session:
        return redirect("/")
    userid = user_id
    userset = {"User" : User.objects.get(id=userid)}
    return render(request, "login_app/userX.html", userset)
def ninjaGold(request):
    if "logged_in" not in request.session:
        return redirect("/")
    content = {"gold" : User.objects.get(id=request.session['id'])}
    return render(request, "login_app/ninjagold.html", content)
def Mine(request):
    goldGen(request.POST["type"], request.session['id'], request)
    return redirect("/ninjagold")
