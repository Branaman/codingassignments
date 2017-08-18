from __future__ import unicode_literals
import re
from django.db import models
from django.contrib import messages
from ..login_app.models import User
from ..books_app.models import Book, Author, Review
def ErrorCheck(request, type, bookid=None):
    result = {"fail" : True, "errors" : None}
    if type == "Register":
        result['errors'] = User.objects.reg_validator(request.POST)
    if type == "Login":
        result['errors'] = User.objects.login_validator(request.POST)
    if type == "Book":
        result['errors'] = Book.objects.book_validator(request.POST)
    if type == "Author":
        result['errors'] = Author.objects.author_validator(request.POST)
    if type == "Review":
        result['errors'] = Review.objects.review_validator(request.POST)
    if len(result['errors']):
        for error in result['errors'].itervalues():
            messages.add_message(request, messages.ERROR, error)
    else:
        result['fail'] = False
    return result
