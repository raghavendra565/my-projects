from django.shortcuts import render
from MainApp.models import Users
from MainApp.serializers.users import UsersSerializer
from django.core import serializers
from django.http import HttpResponse,JsonResponse,Http404
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework import status
import crypt



class getupdatedeleteusers(APIView):
    def get_object(self, id):
        try:
            return Users.objects.get(id=id)
        except :
            raise Http404
    def get(self, request, id, format=None):
        try:
            cat = self.get_object(id)
            serializer = UsersSerializer(cat)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"user not found"})
    def put(self, request, id, format=None):
        try:
            cat = self.get_object(id)
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            mobile = request.data['mobile']
            email = request.data['email']
            password = crypt.crypt(request.data['password'])
            print("password:",password)
            address = request.data['address']
            role=request.data['role']
            status = request.data['status']
            user = {'first_name':first_name,'last_name':last_name,'mobile':mobile,'email':email,'password': password,'address':address,'role':role,'status':status}
            print("dictonary:",user)
            serializer = UsersSerializer(cat,data=user)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({"message:":"user not updated"})
    def delete(self, request, id, format=None):
        try:
            cat = self.get_object(id)
            cat.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except :
            return JsonResponse({"message:":"user not deleted"})
