from rest_framework import serializers
from MainApp.models import Listing_images



class Listing_imagesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Listing_images
        fields= '__all__'
