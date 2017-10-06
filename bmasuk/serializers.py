from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from  models import Bmasuk


class BmasukSerializer(serializers.ModelSerializer):
    class Meta :
        model = Bmasuk
        fields=('__all__')
        depth=1