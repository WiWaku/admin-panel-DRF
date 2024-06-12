from .models import Reviews_model
from rest_framework import serializers


class RevSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews_model
        fields = ['rev_Img']
