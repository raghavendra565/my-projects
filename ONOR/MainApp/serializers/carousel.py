from rest_framework import serializers
from MainApp.models import Carousel



class CarouselSerializer(serializers.ModelSerializer):
    class Meta():
        model = Carousel
        fields= '__all__'
