from rest_framework import viewsets
from solitude.models.clustermodel import Cluster

class ClusterView(viewsets.ModelViewSet):
    queryset = Cluster.objects.all()