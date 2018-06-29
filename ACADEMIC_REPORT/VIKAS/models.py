# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class StudentMarks(models.Model):
    student_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    marks = models.IntegerField()


class SubjectFaculty(models.Model):
    subject = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
