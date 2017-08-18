# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from ..login_app.models import User
from ..books_app.models import Book, Review, Author
from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
def specUser(request, user_id):
    if "loggedIn" in request.session and request.session['loggedIn'] == True:
        userid = user_id
        userset = {"User" : User.objects.get(id=userid)}
        return render(request, "users_app/index.html", userset)
    else:
        return redirect("/")
