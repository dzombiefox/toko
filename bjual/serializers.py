from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from  models import Bjual


class BjualSerializer(serializers.ModelSerializer):
    class Meta :
        model = Bjual
        fields=('__all__')
        depth=1