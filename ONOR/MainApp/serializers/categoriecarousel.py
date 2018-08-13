from rest_framework import serializers
from MainApp.models import Categoriecarousel




class CategoriecarouselSerializer(serializers.ModelSerializer):
    class Meta():
        model = Categoriecarousel
        fields= '__all__'
