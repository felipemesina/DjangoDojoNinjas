# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0003_auto_20170921_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='books',
            field=models.ManyToManyField(related_name='joinedTable', to='book_authors.books'),
        ),
    ]
