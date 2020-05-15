"""gmlews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restapi import views

from django.contrib.auth.models import User
from restapi.models import Data, Node, Post
from rest_framework import routers

from restapi.views import DataViewSet, MapView, NodeViewSet, Charts, Map, ChartsDua, AcceleroXViewSet, ChartNode, TambahNode, PostViewSet


router = routers.DefaultRouter()

router.register(r'data', DataViewSet, 'data')

router.register(r'node', NodeViewSet, 'node')

router.register(r'map', MapView, 'map')

router.register(r'accelerox', AcceleroXViewSet, 'accelerox')

router.register(r'post', PostViewSet, 'post')


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', include(router.urls)),
    path(r'', include('rest_framework.urls', namespace='rest_framework')),
    path('charts/', Charts.as_view(), name='charts'),
    path('charts2/', ChartsDua.as_view(), name='charts2'),
    path('chartnode/', ChartNode.as_view(), name='chartnode'),
    path('map/', Map.as_view(), name='map'),
    path('addnode/', views.add_node, name='add-node'),
    path('node/', TambahNode.as_view(), name='tambahnode'),

]
