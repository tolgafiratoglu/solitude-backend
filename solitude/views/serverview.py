from rest_framework import viewsets
from django.http import HttpResponse
from django.core import serializers
from solitude.models.servermodel import Server

from solitude.serializers.serverserializer import ServerSerializer

class ServerView(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
