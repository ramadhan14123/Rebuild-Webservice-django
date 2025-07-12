from rest_framework import serializers
from .models import TBCarsWeb

class TBCarsWebSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBCarsWeb
        fields = '__all__' 