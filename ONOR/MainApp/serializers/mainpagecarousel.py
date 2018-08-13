from rest_framework import serializers
from MainApp.models import MainpageCarousel


class MainpageCarouselSerializer(serializers.ModelSerializer):
    class Meta():
        model = MainpageCarousel
        fields= '__all__'
