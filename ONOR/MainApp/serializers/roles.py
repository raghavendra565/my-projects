from rest_framework import serializers
from MainApp.models import Roles


class RolesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Roles
        fields= '__all__'
