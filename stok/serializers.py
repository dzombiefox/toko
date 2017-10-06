from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from  models import Stok


class StokSerializer(serializers.ModelSerializer):
    class Meta :
        model = Stok
        fields=('__all__')
        depth=1