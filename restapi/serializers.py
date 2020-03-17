from .models import Data,Node
from rest_framework import serializers


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
    

class NodeSerializer(serializers.ModelSerializer):
    class Meta :
        model = Node
        fields = '__all__'