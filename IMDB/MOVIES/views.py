# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse,HttpResponseNotFound
from MOVIES.models import Movies

def getmovies(request):
    movies = Movies.objects.all()
    if movies:
        context = {
        'movies': movies
        }
        return render(request,'movies.html',context)
    else:
        return HttpResponseNotFound("movie not found")

def getdirector(request,_director):
    _director = _director.replace("%"," ")
    movies = Movies.objects.filter(director = _director)
    if movies:
        context = {
        'movies': movies
        }
        return render(request,'movies.html',context)
    else:
        return HttpResponseNotFound("movie not found")
