# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
def login(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    print "login page opened"
    return render(request, "third_app/index.html", context)
def newUser(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    print "registration page opened"
    return render(request, "third_app/newUser.html", context)
def users(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    print "users page opened"
    return render(request, "third_app/users.html", context)
