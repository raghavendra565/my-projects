from rest_framework import serializers
from MainApp.models import Users
from django.contrib.auth.hashers import make_password
import crypt


class UsersSerializer(serializers.ModelSerializer):
    class Meta():
        model = Users
        fields= ('first_name','last_name','mobile','email','password','address','role','status')

        
    """def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        mobile = validated_data['mobile']
        email = validated_data['email']
        password = make_password['plaintext_password']
        address = validated_data['address']
        role = validated_data['role']
        status = validated_data['status']
        obj = Users(first_name=first_name,last_name=last_name,mobile=mobile,email=email,password=password,address=address,role=role,status=status)
        obj.save()
        return obj"""






    """    fields= ('first_name','last_name','mobile','email','password','address','role','status')
    def create(self, validated_data):
        first_name = validated_data(first_name)
        last_name = validated_data(last_name)
        mobile = validated_data(mobile)
        email = validated_data(email)
        password = crypt.crypt(validated_data(password))
        address = validated_data(address)
        role = validated_data(role)
        status = validated_data(status)
        obj = Users(first_name=first_name,last_name=last_name,mobile=mobile,email=email,password=password,address=address,role=role,status=status)
        obj.save()
        return obj"""
