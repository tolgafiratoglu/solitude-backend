from rest_framework import serializers
from solitude.models.servermodel import Server

class ServerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = ('id', 'active', 'host', 'port', 'notes')
