# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
def index(request):
    print "blog index page opened"
    return render(request, "first_app/index.html")
def numPage(request, number):
    number = {'number' : number}
    print "blog num, page opened", number
    return render(request, "first_app/pagenum.html", number)
def editPage(request, number):
    number = {'number' : number}
    print "blog edit, page opened", number
    return render(request, "first_app/edit.html", number)
def delPage(request, number):
    number = {'number' : number}
    print "blog del, page opened", number
    return render(request, "first_app/delete.html", number)
def create(request):
    print "blog create page opened"
    return render(request, "first_app/index.html")
def new(request):
    print "blog new page opened"
    return render(request, "first_app/new.html")
