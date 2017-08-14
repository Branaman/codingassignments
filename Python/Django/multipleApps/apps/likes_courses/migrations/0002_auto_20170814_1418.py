# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('likes_courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='liked_books',
        ),
        migrations.RemoveField(
            model_name='user',
            name='uploaded_books',
        ),
        migrations.AddField(
            model_name='book',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_books', to='likes_courses.User'),
        ),
        migrations.AddField(
            model_name='book',
            name='uploader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_books', to='likes_courses.User'),
            preserve_default=False,
        ),
    ]
