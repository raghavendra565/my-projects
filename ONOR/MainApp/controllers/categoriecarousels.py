from django.shortcuts import render
from MainApp.models import Categoriecarousel
from MainApp.serializers.categoriecarousel import CategoriecarouselSerializer
from django.core import serializers
from django.http import HttpResponse,JsonResponse,Http404
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework import status




"""@api_view(['GET'])
def getcatcaro(request):
    s=Catcarousel.objects.all()
    if s:
        obj= CatcarouselSerializer(s,many= True)
        return Response(obj.data)"""

class getupdatedeletecategoriecarousels(APIView):
    def get_object(self, id):
        try:
            return Categoriecarousel.objects.get(id=id)
        except :
            raise Http404
    def get(self, request, id, format=None):
        try:
            cat = self.get_object(id)
            serializer = CategoriecarouselSerializer(cat)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"categorie carousel not found"})
    def put(self, request, id, format=None):
        try:
            cat = self.get_object(id)
            serializer = CategoriecarouselSerializer(cat, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({"message:":"categorie carousel not updated due to some problems, carouse not found or field may be not found"})
    def delete(self, request, id, format=None):
        try:
            cat = self.get_object(id)
            cat.delete()
            return JsonResponse({"message:":"catcarousel  is deleted"})
        except :
            return JsonResponse({"message:":"categorie carousel not deleted"})
