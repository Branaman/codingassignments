# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "first_app/index.html", context)
