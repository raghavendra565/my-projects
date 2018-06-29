# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import square
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseNotFound
from .serializers import squareSerializer
import MySQLdb

HOST = 'localhost'
USER = 'ganesh'
PASSWORD = 'ganesh55'
DATABASE = 'sqr'

# Create your views here.
@api_view(['GET'])
def getnum(request, _num):
    _mar = square.objects.filter(number = _num)
    if _mar:
        serializer = squareSerializer(_mar, many = True)
        return Response(serializer.data)
    else:
        _sq = int(_num) * int(_num)
        db=MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE)
        cursor = db.cursor()
        cursor.execute('INSERT INTO Squares_square (number, sqr) values(%s, %s)',(float(_num),float(_sq)))
        db.commit()
        cursor.close()
        print (_sq)
        return Response({'Message': "New number and it's square inserted", 'Number': _num, 'Square': _sq})

@api_view(['GET'])
def getsquare(request,_num):
    _num = _num.replace('%', ' ')
    sqr=square.objects.filter(number=_num)
    if sqr:
		serializer=squareSerializer(sqr,many=True)
		return Response(serializer.data)
    else:
        return Response({"Message": 'NUMBER NOT FOUND'})

@api_view(['GET'])
def post(request, _values):
    _num, _sq = _values.split('-')
    _mar = square.objects.filter(number = _num)
    if _mar:
        db=MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE)
        cursor = db.cursor()
        cursor.execute('UPDATE Squares_square SET sqr = %s WHERE number = %s',(float(_sq),float(_num)))
        db.commit()
        cursor.close()
        print (_sq)
        return Response({'Message': 'Square of the given number is updated', 'Number': _num, 'Square': _sq})
    else:
        db=MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE)
        cursor = db.cursor()
        cursor.execute('INSERT INTO Squares_square (number, sqr) values(%s, %s)',(float(_num),float(_sq)))
        db.commit()
        cursor.close()
        print (_sq)
        return Response({'Message': 'New number and square inserted', 'Number': _num, 'Square': _sq})
