# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect
import random
import time
monOyear = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
def index(request):
    if "logged_in" in request.session:
        return redirect("/dash")
    return render(request, "login_app/index.html")
def register(request):
    results = User.objects.ErrorCheck(request, "Register")
    if results['pass']:
        User.objects.createUser(request)
        return redirect("/dash")
    else:
        return redirect("/")
def login(request):
    results = User.objects.ErrorCheck(request, "Login")
    if results['pass']:
        sessionUpdate(request)
        return redirect("/dash")
    else:
        return redirect("/")
def logout(request):
    request.session.clear()
    return redirect('/')
def dash(request):
    if "logged_in" not in request.session:
        return redirect("/")
    months = {}
    for count in range(0,13):
        month = monOyear[count-1]
        months[str(month)] = User.objects.all().filter(dob__month=count).order_by('dob')
    return render(request, "login_app/dash.html", months)
def users(request):
    if "logged_in" not in request.session:
        return redirect("/")
    users = {"Users": User.objects.all().order_by('dob')}
    return render(request, "login_app/users.html", users)
def userX(request, user_id):
    if "logged_in" not in request.session:
        return redirect("/")
    userid = user_id
    userset = {"User" : User.objects.get(id=userid)}
    return render(request, "login_app/userX.html", userset)
def test(request):
    def randomWord(num):
        vowel = ("u", "a", "ae", "e", "eh", "ur", "i", "ee", "o", "ah", "ou", "oo", "ow", "ei", "oy", "ai", "er", "ure")
        consonant = ("b", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ing", "p", "r", "s", "sh", "t", "ch", "th", "ge", "si", "z", "v", "w")
        word = ""
        for count in range(0, num/2):
            word += str(random.choice(vowel)) + str(random.choice(consonant))
            if len(word)>num:
                break
        return word[:num]
    def strTimeProp(start, end, formating, prop):
        # """Get a time at a proportion of a range of two formatted times.
        #
        # start and end should be strings specifying times formated in the
        # given format (strftime-style), giving an interval [start, end].
        # prop specifies how a proportion of the interval to be taken after
        # start.  The returned time will be in the specified format.
        # """
        stime = time.mktime(time.strptime(start, formating))
        etime = time.mktime(time.strptime(end, formating))
        ptime = stime + prop * (etime - stime)
        return time.strftime(formating, time.localtime(ptime))
    def randomDate(start, end, prop):
        return strTimeProp(start, end, '%Y-%m-%d', prop)

    for value in range(1,100):
        User.objects.create(first_name=str(randomWord(6)), last_name=str(randomWord(12)), email= str(randomWord(6))+"@gmail.com", password="charliefoxtrot", dob=randomDate("1970-8-22", "1999-8-22", random.random())  )
    return render(request, "login_app/index.html")
