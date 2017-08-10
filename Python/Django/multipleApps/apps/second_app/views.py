# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
def surveys(request):
    print "second page opened"
    return render(request, "second_app/surveys.html")
def addSurvey(request):
    print "second page opened"
    return render(request, "second_app/newSurvey.html")
