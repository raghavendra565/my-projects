from rest_framework import serializers
from MainApp.models import Listings



class ListingsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Listings
        fields= '__all__'
