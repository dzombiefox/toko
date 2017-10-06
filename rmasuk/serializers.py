from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from  models import Rmasuk
from bmasuk .models import Bmasuk


# class Bmasukserializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bmasuk
#         fields = ('__all__')


class RmasukSerializer(serializers.ModelSerializer):
    # feed = Bmasukserializer(many=True)
    class Meta :
        model = Rmasuk
        fields=('__all__')
        depth=1