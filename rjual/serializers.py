from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from  models import Rjual
from bjual .models import Bjual
class BarangJualSerializer(serializers.RelatedField):
    class Meta:
        model=Bjual
        fields =('__all__')
        # depth = 1

class RjualSerializer(serializers.ModelSerializer):
    # tracks = BarangJualSerializer(many=True)
    class Meta :
        model = Rjual
        fields=('__all__')
        # depth=1