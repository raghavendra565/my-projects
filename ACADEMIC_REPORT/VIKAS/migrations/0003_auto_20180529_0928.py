# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIKAS', '0002_auto_20180529_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectfaculty',
            name='subject',
            field=models.CharField(max_length=30),
        ),
    ]
