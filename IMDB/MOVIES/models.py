# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movies(models.Model):
    popularity = models.CharField(max_length=50, null=True)
    director = models.CharField(max_length=50, null=True)
    genre = models.CharField(max_length=50, null=True)
    movielist_score = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    dt_added        = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dt_updated      = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __unicode__(self):
       return  self.name
