# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class formManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors["name"] = "Course Name should be more than 0 characters"
        if len(postData['desc']) < 1:
            errors["desc"] = "please input a description"
        return errors;
class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = formManager()
    def __str__(self):
        return "%s %s" % (self.name, self.desc)

# Create your models here.
