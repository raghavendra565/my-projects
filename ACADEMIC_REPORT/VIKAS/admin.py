# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import StudentMarks, SubjectFaculty

class StudentMarksDetail(admin.ModelAdmin):
    list_display = ('student_name','subject','marks')

admin.site.register(StudentMarks,StudentMarksDetail)
# Register your models here.
class SubjectFacultyDetail(admin.ModelAdmin):
    list_display = ('subject', 'name')

admin.site.register(SubjectFaculty, SubjectFacultyDetail)
