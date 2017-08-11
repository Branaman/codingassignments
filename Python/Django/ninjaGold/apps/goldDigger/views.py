# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import models
# Create your views here.
def index(request):
    if "gold" not in request.session.keys():
        request.session['gold'] = 0
    if "log" not in request.session.keys():
        request.session['log'] = ""
    content = { "gold" : request.session['gold'],}
    print "home index page opened"
    return render(request, "goldDigger/index.html", content)

def getGold(request):
    keys = request.POST["type"]
    gold = models.goldGen(keys)
    request.session["log"] += models.act_logs(keys, gold)
    request.session["gold"] += gold
    return render(request, "goldDigger/index.html")

def reset(request):
    request.session.clear()
    return redirect("/")
