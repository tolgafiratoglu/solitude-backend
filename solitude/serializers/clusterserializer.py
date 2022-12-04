from rest_framework import serializers

from solitude.models.clustermodel import Cluster

class ClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cluster
        fields = ('id', 'title', 'notes', )