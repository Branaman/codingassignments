# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
def index(request):
    print "first page opened"
    return render(request, "first_app/index.html")
def numPage(request, number):
    number = {'number' : number}
    print "num, page opened", number
    return render(request, "first_app/pagenum.html", number)
def editPage(request, number):
    number = {'number' : number}
    print "num, page opened", number
    return render(request, "first_app/edit.html", number)
def delPage(request, number):
    number = {'number' : number}
    print "num, page opened", number
    return render(request, "first_app/delete.html", number)
def create(request):
    return render(request, "first_app/index.html")
def new(request):
    return render(request, "first_app/new.html")
