from django.shortcuts import render
from MainApp.models import Listing_images
from MainApp.serializers.listing_images import Listing_imagesSerializer
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework import status






class createlisting_images(APIView):

    def get(self, request,*args,**kwargs):
        user = Listing_images.objects.all()
        serializer = Listing_imagesSerializer(user, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = Listing_imagesSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
