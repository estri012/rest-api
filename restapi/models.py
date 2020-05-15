from django.db import models
import json

# Create your models here.
class Data(models.Model):
    node_id = models.ForeignKey("Node", on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    vibration = models.IntegerField()
    moisture = models.IntegerField()
    gps_latitude = models.CharField(max_length=250)
    gps_longitude = models.CharField(max_length=250)
    gyro_x = models.FloatField()
    gyro_y = models.FloatField()
    gyro_z = models.FloatField()
    accelero_x = models.FloatField()
    accelero_y = models.FloatField()
    accelero_z = models.FloatField()
    displacement = models.IntegerField()


class Node(models.Model):
    node_id = models.IntegerField(primary_key=True)
    latitude = models.CharField(max_length=250)
    longitude = models.CharField(max_length=250)
    location = models.CharField(max_length=500)

class Post(models.Model):
    contact = models.IntegerField(primary_key=True)
    acs = models.CharField(max_length=250)
    ais = models.CharField(max_length=250)
    aes = models.CharField(max_length=250)