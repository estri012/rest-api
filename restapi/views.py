import json
from django.views.generic import View
from django.http import Http404
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from restapi.serializers import DataSerializer, NodeSerializer, AcceleroXSerializer, PostSerializer
from restapi.models import Data, Node, Post
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from rest_framework.views import APIView
# Create your views here.
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect

class Charts(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')

class ChartsDua(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts2.html')

class ChartNode(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chartnode.html')

class Map(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'map.html')

class TambahNode(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'node.html')
        

def list(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'list.html', context)

def addnode(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'node.html', context)

def base(request):
    sensor_list = Node.objects.order_by('node_name')
    context = {'sensor_list': sensor_list}
    return render(request, 'base.html', context)

def chartsensor(request):
    sensor_list = Node.objects.order_by('node_name')
    context = {'sensor_list': sensor_list}
    return render(request, 'chartbaru.html', context)

def shownode(request, node_node_id):
    try:
        node = Node.objects.get(pk=node_node_id)
    except Node.DoesNotExist:
        raise Http404("Node does not exist")
    return render(request, 'chartbaru.html', {'node': node})

def accelero_x(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'accelero_x.html', context)

def accelero_y(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'accelero_y.html', context)

def accelero_z(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'accelero_z.html', context)

def gyro_x(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'gyro_x.html', context)

def gyro_y(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'gyro_y.html', context)

def gyro_z(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'gyro_z.html', context)

def moisture(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'moisture.html', context)

def vibration(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'vibration.html', context)

def displacement(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'displacement.html', context)

def angular(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'angular.html', context)



class DataViewSet(viewsets.ModelViewSet):
        queryset = Data.objects.all()
        serializer_class = DataSerializer
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['node_id']


class MapView(viewsets.ModelViewSet):
        queryset = Data.objects.filter(node_id=1).order_by('-id')[:1]
        serializer_class = DataSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['node_id']

class AcceleroXViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = AcceleroXSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

def add_node(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Permintaan menambah node baru dari {form.cleaned_data["username"]}'
            message = f'Pemohon: {form.cleaned_data["email"]}\nLokasi node: {form.cleaned_data["lokasi_pemasangan_node"]}\nPJ: {form.cleaned_data["penanggung_jawab_pemasangan"]}\nKontak PJ: {form.cleaned_data["no_telp_penanggung_jawab"]}\nTanggal pemasangan: {form.cleaned_data["tanggal_pemasangan_node"]}\nSensor node: {form.cleaned_data["sensor_yang_digunakan_pada_node"]}'
            sender = form.cleaned_data["email"]
            recipients = ['gmlews.ugm@gmail.com']
            try:
                send_mail(subject, message, sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect(add_node)
    return render(request, 'addnode.html', {'form':form})


