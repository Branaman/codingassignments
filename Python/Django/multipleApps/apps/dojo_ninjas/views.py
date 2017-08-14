# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
def login(request):
    print "Login page opened"
    return render(request, "third_app/index.html")
def newUser(request):
    print "new User page opened"
    return render(request, "third_app/newUser.html")
def users(request):
    print "users page opened"
    return render(request, "third_app/users.html")
