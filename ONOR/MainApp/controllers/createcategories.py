from django.shortcuts import render
from MainApp.models import Categories
from MainApp.serializers.categorie import CategoriesSerializer
from django.core import serializers
from django.http import HttpResponse,JsonResponse,Http404
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework import status




"""@api_view(['POST'])
def postcategories(request):
    s=CategoriesSerializer(data=request.data)
    print(s)
    if s.is_valid():
        s.save()
        return Response(s.data, status= 301)"""

class createcategories(APIView):

    def get(self, request,*args,**kwargs):
        user = Categories.objects.all()
        serializer = CategoriesSerializer(user, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CategoriesSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
