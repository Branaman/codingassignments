from __future__ import unicode_literals
import re
from django.db import models
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import bcrypt
def ErrorCheck(request, type):
    result = {"fail" : True, "errors" : None}
    if type == "Comment":
        result['errors'] = User.objects.comment_validator(request.POST)
    if type == "Login":
        result['errors'] = User.objects.login_validator(request.POST)
    else:
        result['fail'] = False
    return result

def sessionUpdate(postData):
    request.session['id'] = User.objects.get(age=postData['age'],name=postData['user_name']).id
    request.session['loggedIn'] = True
class formManager(models.Manager):
    def login_validator(self, postData):
        errors = {}
        if len(postData['user_name']) < 2:
            errors["user_name"] = "Name should be more than 1 character"
        if len(postData['age']) < 1:
            errors["age"] = "please enter your age"
        print "made it to the balidator!"
        if len(User.objects.filter(age=postData['age'],name=postData['user_name'])) < 1:
            sessionUpdate(postData)
            print "user exists! "
        else:
            print "tried to make a user"
            User.objects.create(user_name=postData['user_name'], age=postData['age'],)
            sessionUpdate(postData)
        return errors;
class User(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = formManager()
    def __str__(self):
        return "%s %s" % (self.user_name, self.alias)
