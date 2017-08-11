# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    print "blog index page opened"
    return render(request, "formSubmitter/index.html")
def submitter(request):
    if "counter" not in request.session.keys():
        request.session['counter'] = 0
    request.session['counter'] += 1
    content={
    "name":request.POST['name'],
    "DojoLocation":request.POST['DojoLocation'],
    "comments":request.POST['comments'],
    "favLang":request.POST['favLang'],
    }
    return render(request, "formSubmitter/result.html", content)
