# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    if "counter" not in request.session.keys():
        request.session['counter'] = 0
    if "formdata" not in request.session.keys():
        request.session['formdata'] = ""
    print "home index page opened"
    return render(request, "formSubmitter/index.html")
def submitter(request):
    request.session['counter'] += 1
    if 'size' not in request.POST:
        textsize = '5'
    else:
        textsize = request.POST['size']
    formdata = str("<h2 class='" + request.POST['color'] + " text-darken-2'><font size='" + textsize + "'>" + request.POST['name'] + "</font></h2>")
    print formdata
    request.session['formdata'] += formdata
    content={
    "formdata": request.session['formdata'],
    }
    print request.session['formdata']
    return render(request, "formSubmitter/index.html", content)
