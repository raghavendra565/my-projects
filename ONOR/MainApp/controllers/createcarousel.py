from django.shortcuts import render
from MainApp.models import Carousel
from MainApp.serializers.carousel import CarouselSerializer
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework import status


"""@api_view(['POST'])
def postcarousels(request):
    s=CarouselSerializer(data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data, status= 301)"""

class createcarousels(APIView):

    def get(self, request,*args,**kwargs):
        user = Carousel.objects.all()
        serializer = CarouselSerializer(user, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CarouselSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
