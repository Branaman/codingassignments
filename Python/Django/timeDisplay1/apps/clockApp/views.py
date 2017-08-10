# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def clock(request):
    context = {
    "date": strftime("%b %d, %Y", gmtime()),
    "time": strftime("%H:%M:%S %p", gmtime()),
    }
    return render(request,'clockApp/page.html', context)
