from django.shortcuts import render
from MainApp.models import Roles
from MainApp.serializers.roles import RolesSerializer
from django.core import serializers
from django.http import HttpResponse,JsonResponse,Http404
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework import status


class getupdateroles(APIView):
    def get_object(self, id):
        try:
            return Roles.objects.get(id=id)
        except :
            raise Http404
    def get(self, request, id, format=None):
        try:
            cat = self.get_object(id)
            serializer = RolesSerializer(cat)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"roles  not found"})
    def put(self, request, id, format=None):
        try:
            cat = self.get_object(id)
            serializer = RolesSerializer(cat, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({"message":"roles  not updated due to some problems or listing not found or field may be not found"})
