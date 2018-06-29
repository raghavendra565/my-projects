# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Movies

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('popularity', 'director', 'genre', 'movielist_score', 'name')
    search_fields = ('popularity', 'director', 'genre', 'movielist_score', 'name')

admin.site.register(Movies,MoviesAdmin)
