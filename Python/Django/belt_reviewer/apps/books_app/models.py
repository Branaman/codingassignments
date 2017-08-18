from __future__ import unicode_literals
import re
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib import messages
from ..login_app.models import User
import bcrypt
class formManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['book_title']) < 2:
            errors["book_title"] = "Book Title should be more than 1 character"
        print "validation completed"
        return errors;
    def author_validator(self, postData):
        errors = {}
        if len(self.filter(author_name= postData['author_name'],)) > 0:
            errors['author'] = "this author already exists"
        if len(postData['author_name']) < 2:
            errors["author_name"] = "Author Name should be more than 1 character"
        print "validation completed"
        return errors;
    def review_validator(self, postData):
        errors = {}
        if len(postData['stars']) < 1:
            errors["stars"] = "Review must include a rating"
        if len(postData['content']) < 1 or len(postData['content']) > 255:
            errors["content"] = "Review length must be between 1 and 255 characters"
        print "validation completed"
        return errors;
class creators(models.Manager):
    def authorCreate(self, request, result):
        Author.objects.create(author_name=request.POST['author_name'],)
        result['errors'] = {'success': "Author added successfully!"}
        messages.add_message(request, messages.ERROR, result['errors']['success'])
        request.session['authorid'] = Author.objects.get(author_name=request.POST['author_name']).id
        def __str__(self):
            return "%s" % (self.name)
    def bookCreate(self, request, result,):
        Book.objects.create(book_title=request.POST['book_title'],author=Author.objects.get(id=request.session['authorid']),)
        result['errors'] = {'success': "Book added successfully!"}
        messages.add_message(request, messages.ERROR, result['errors']['success'])
        request.session['bookid'] = Book.objects.filter(book_title=request.POST['book_title']).first().id
    def reviewCreate(self, request, result,):
        Review.objects.create(content=request.POST['content'],stars=request.POST['stars'],book=Book.objects.get(id=request.session['bookid']),user=User.objects.get(id=request.session['id']),)
        result['errors'] = {'success': "Review added successfully!"}
        messages.add_message(request, messages.ERROR, result['errors']['success'])
        def __str__(self):
            return "%s" % (self.text, self.stars)
class Author(models.Model):
    author_name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = formManager()
    creation = creators()
class Book(models.Model):
    book_title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, related_name = "books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = formManager()
    creation = creators()
    def __str__(self):
        return "%s" % (self.book_title)
class Review(models.Model):
    content = models.TextField()
    stars = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    book = models.ForeignKey(Book, related_name = "reviews")
    user = models.ForeignKey(User, related_name = "reviews")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = formManager()
    creation = creators()
