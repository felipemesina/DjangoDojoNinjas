# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 00:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notes',
            field=models.TextField(default=False),
        ),
    ]
