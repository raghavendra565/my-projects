from django.shortcuts import render
from MainApp.models import Listings
from MainApp.serializers.listing import ListingsSerializer
from django.core import serializers
from django.http import HttpResponse,JsonResponse,Http404
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework import status


class getupdatedeletelistings(APIView):
    def get_object(self, id):
        try:
            return Listings.objects.get(id=id)
        except :
            raise Http404
    def get(self, request, id, format=None):
        try:
            cat = self.get_object(id)
            serializer = ListingsSerializer(cat)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"listings not found"})
    def put(self, request, id, format=None):
        try:
            cat = self.get_object(id)
            serializer = ListingsSerializer(cat, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({"message":"listings not updated due to some problems or listing not found or field may be not found"})
    def delete(self, request, id, format=None):
        try:
            cat = self.get_object(id)
            cat.delete()
            return JsonResponse({"message:":"listings is deleted"})
        except :
            return JsonResponse({"message:":"listings not deleted"})
