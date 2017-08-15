from __future__ import unicode_literals
import re
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import bcrypt
class formManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be more than 1 character"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be more than 1 character"
        if not re.match(r"[^@]+@[^@]+\.[^@]+$", postData['email']):
            errors["email"] = "Must use a valid Email"
        if len(postData['password']) < 8:
            errors["password"] = "password requires minimum 8 characters"
        try:
            if User.objects.get(email=postData['email']):
                errors['email'] = "this user already exists"
        except ObjectDoesNotExist:
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
            errors['email'] = "Please Register"
            print "email isnt there"
        return errors;
class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = formManager()
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
