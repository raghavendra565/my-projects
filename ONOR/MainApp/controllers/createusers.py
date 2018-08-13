from django.shortcuts import render
from MainApp.models import Users
from MainApp.serializers.users import UsersSerializer
from django.core import serializers
from django.http import HttpResponse,JsonResponse,Http404
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework import status
import crypt




class createusers(APIView):

    def get(self, request,*args,**kwargs):
        user = Users.objects.all()
        serializer = UsersSerializer(user, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None,*args,**kwargs):
     print("posting data:",request.data)
     serializer = UsersSerializer(data=request.data)
     print (serializer)
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
     serializer = UsersSerializer(data=user)
     if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
