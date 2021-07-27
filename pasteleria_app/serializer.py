from rest_framework import serializers
from .models import Pasteles


class PastelesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasteles
        fields = '__all__'
