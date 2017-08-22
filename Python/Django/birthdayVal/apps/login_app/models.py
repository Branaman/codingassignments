from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import bcrypt
from random import randint
import re
from datetime import date, timedelta
import datetime
def sessionUpdate(request):
    print request.POST, "HI"
    request.session['name'] = User.objects.get(email=request.POST['email']).first_name
    request.session['id'] = User.objects.get(email=request.POST['email']).id
    request.session['logged_in'] = True
class formManager(models.Manager):
    def ageCalc(self, birthdate):
        today = date.today()
        birthday = datetime.datetime.strptime(birthdate, '%Y-%m-%d')
        if (today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))) < 18:
            return False
        return True
    def ErrorCheck(self, request, type):
        result = {"pass" : False, "errors" : None}
        if type == "Register":
            result['errors'] = User.objects.reg_validator(request.POST)
        if type == "Login":
            result['errors'] = User.objects.login_validator(request.POST)
        if len(result['errors']):
            for error in result['errors'].itervalues():
                messages.add_message(request, messages.ERROR, error)
        else:
            result['pass'] = True
        return result
    def createUser(self, request):
        charliefoxtrot = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email= request.POST['email'], password=charliefoxtrot, dob=request.POST['dob'])
        print request.POST
        sessionUpdate(request)
    def reg_validator(self, postData):
        errors = {}
        if postData['password']!=postData['c_password']:
            errors["confirm"] = "Passwords do not match"
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First should be more than 1 character"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be more than 1 character"
        if not re.match(r"[^@]+@[^@]+\.[^@]+$", postData['email']):
            errors["email"] = "Must use a valid Email"
        if not User.objects.ageCalc(postData['dob']):
            errors["dob"] = "Must be 18 years of age to register"
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
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    dob = models.DateField()
    activities = models.TextField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = formManager()
    def __str__(self):
        return "%s %s, %s" % (self.first_name, self.last_name, self.dob)
