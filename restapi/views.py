from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from restapi.serializers import UserSerializer, DataSerializer, NodeSerializer
from django.contrib.auth.models import User
from restapi.models import Data, Node
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
