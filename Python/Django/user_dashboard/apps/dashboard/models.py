# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class formManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["name"] = "first name should be more than 0 characters"
        if len(postData['last_name']) < 1:
            errors["desc"] = "last name should be more than 0 characters"
        if len(postData['email']) < 6:
            errors["desc"] = "email should be more than 5 characters"
        return errors;
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = formManager()
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
