from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from  models import Biaya

class BiayaSerializer(serializers.ModelSerializer):
    class Meta :
        model = Biaya
        fields=('__all__')
        depth=1