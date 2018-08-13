from django.shortcuts import render
from MainApp.models import Categoriecarousel
from MainApp.serializers.categoriecarousel import CategoriecarouselSerializer
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework import status




"""@api_view(['POST'])
def postcatcarousels(request):
    s=CatcarouselSerializer(data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data, status= 301)"""

class createcategoriecarousels(APIView):

    def get(self, request,*args,**kwargs):
        user = Categoriecarousel.objects.all()
        serializer = CategoriecarouselSerializer(user, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CategoriecarouselSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
