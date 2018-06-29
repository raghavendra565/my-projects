# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.shortcuts import render
from VIKAS.models import StudentMarks, SubjectFaculty
from django.http import HttpResponse, HttpResponseNotFound



def getstudent(request):
    object = StudentMarks.objects.first()
    return HttpResponse('<H1> ' +str(object)+'</H1>')

def getfaculty(request):
    object = SubjectFaculty.objects.first()
    return HttpResponse('<H1> ' +str(object)+'</H1>')

def studentdata(request):
    students = StudentMarks.objects.all()
    if students:
        context = {
            'students': students
        }
        return render(request, 'student.html', context)
    else:
        return HttpResponseNotFound("student not found")


def facultydata(request):
    faculty = SubjectFaculty.objects.all()
    if faculty:
        context = {
            'faculty': faculty
        }
        return render(request, 'student.html', context)
    else:
        return HttpResponseNotFound("Article not found")

def getstudentid(request,_id):
    print (_id)
    students = StudentMarks.objects.filter(id =_id)
    if students:
        context = {
            'students': students
        }
        return render(request, 'student.html', context)
    else:
        return HttpResponseNotFound("student not found")


def getsubject(request,_subject):
    _subject = _subject.replace('%', ' ')

    students = StudentMarks.objects.filter(subject =_subject)
    if students:
        context = {
            'students': students
        }
        return render(request, 'student.html', context)
    else:
        return HttpResponseNotFound("student not found")

def getstudentname(request,_studentname):
    _studentname = _studentname.replace('%', ' ')

    students = StudentMarks.objects.filter(student_name =_studentname)
    if students:
        context = {
            'students': students
        }
        return render(request, 'student.html', context)
    else:
        return HttpResponseNotFound("student not found")
