# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('marks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SubjectFaculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
