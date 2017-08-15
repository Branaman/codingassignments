# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *
# Create your views here.
def coursesIndex(request):
    courseSet = {'Courses' : Course.objects.all()}
    return render(request, "courses/index.html", courseSet)
def addCourse(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        return redirect('/')
    else:
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
        return redirect("/")
def confDelCourse(request, userid):
    userid = userid
    courseSet = {'Course' : Course.objects.get(id=userid)}
    print courseSet
    return render(request, "courses/course.html", courseSet)
def delCourse(request):
    a = Course.objects.get(id=request.POST['id'])
    a.delete()
    return redirect("/")
