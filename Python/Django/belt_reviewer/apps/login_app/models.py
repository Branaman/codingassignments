from __future__ import unicode_literals
import re
from django.db import models
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import bcrypt
def sessionUpdate(request):
    request.session['alias'] = User.objects.get(email=request.POST['email']).alias
    request.session['id'] = User.objects.get(email=request.POST['email']).id
    request.session['loggedIn'] = True
class formManager(models.Manager):
    def Create(self, request, result):
        charliefoxtrot = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(user_name=request.POST['user_name'], alias=request.POST['alias'], email= request.POST['email'], password=charliefoxtrot)
        sessionUpdate(request)
    def reg_validator(self, postData):
        errors = {}
        if postData['password']!=postData['confirm_pass']:
            errors["confirm"] = "Passwords do not match"
        if len(postData['user_name']) < 2:
            errors["user_name"] = "Name should be more than 1 character"
        if len(postData['alias']) < 2:
            errors["alias"] = "Alias should be more than 1 character"
        if not re.match(r"[^@]+@[^@]+\.[^@]+$", postData['email']):
            errors["email"] = "Must use a valid Email"
        if len(postData['password']) < 8:
            errors["password"] = "password requires minimum 8 characters"
        if len(self.filter(email= postData['email'])) > 0:
            errors['email'] = "this user already exists"
        print "validation completed"
        return errors;
    def login_validator(self, postData):
        errors = {}
        if not re.match(r"[^@]+@[^@]+\.[^@]+$", postData['email']):
            errors["email"] = "Must use a valid Email"
        try:
            if User.objects.get(email=postData['email']):
                user = User.objects.get(email=postData['email']).password
                if not bcrypt.checkpw(postData['password'].encode(), user.encode()):
                    errors['password'] = "incorrect password"
        except ObjectDoesNotExist:
            errors['email'] = "Email not found, please Register"
            print "email isnt there"
        print "validation completed"
        return errors;
class User(models.Model):
    user_name = models.CharField(max_length=32)
    alias = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = formManager()
    def __str__(self):
        return "%s %s" % (self.user_name, self.alias)
