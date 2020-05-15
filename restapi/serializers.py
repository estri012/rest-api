from .models import Data,Node,Post
from rest_framework import serializers


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
    

class NodeSerializer(serializers.ModelSerializer):
    class Meta :
        model = Node
        fields = '__all__'

class AcceleroXSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['timestamp', 'accelero_x']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'