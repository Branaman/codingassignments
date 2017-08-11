# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from random import randint
import datetime
def act_logs(keys, gold):
    logs= "You visisted the " + keys + " and "
    if gold > 0:
        logs+= "Earned "
    else:
        logs += "lost "
    logs += str(gold) + " Gold at " + str(datetime.datetime.now()) +". <br>"
    return logs
def goldGen(keys):
    gold = {
    "house": randint(2, 5),
    "cave": randint(5, 10),
    "farm": randint(10, 20),
    "casino": randint(-50, 50)
    }
    return gold[keys]
