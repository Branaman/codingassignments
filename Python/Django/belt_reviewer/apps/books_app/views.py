# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from ..users_app.models import ErrorCheck
from django.shortcuts import render, redirect
from django.contrib import messages
def index(request):
    if "loggedIn" in request.session and request.session['loggedIn'] == True:
        test = Book.objects.all().order_by('-created_at')[:3]
        print test
        books = {"books" : Book.objects.all(), "users" : User.objects.all(), "reviews" : Review.objects.all()}
        return render(request, "books_app/index.html", books)
    else:
        return redirect("/")
def addBook(request):
    if "loggedIn" in request.session and request.session['loggedIn'] == True:
        authors = {"authors" : Author.objects.all(), "books": Book.objects.all()}
        return render(request, "books_app/addBook.html", authors)
    else:
        return redirect("/")
def processBook(request):
    if "author_id" not in request.POST:
        result=ErrorCheck(request, "Author")
        if result['fail']:
            return redirect('/books/add')
    if "book_id" not in request.POST:
        result=ErrorCheck(request, "Book")
        if result['fail']:
            return redirect('/books/add')

    if "stars" in request.POST:
            result=ErrorCheck(request, "Review")
    else:
        result['fail'] = True
        messages.add_message(request, messages.ERROR, "Please select a rating")
    if result['fail']:
        return redirect('/books/add')
    else:
        if "author_id" in request.POST:
            request.session['authorid'] = Author.objects.get(id=request.POST['author_id'])
        else:
            Author.creation.authorCreate(request, result)
        if "book_id" in request.POST:
            request.session['bookid']= request.POST['book_id']
        else:
            Book.creation.bookCreate(request, result)
        Review.creation.reviewCreate(request, result)
        return redirect("/books")
