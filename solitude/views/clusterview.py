from rest_framework import viewsets
from solitude.models.clustermodel import Cluster
from kafka.cluster import ClusterMetadata
from django.http import JsonResponse, HttpResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

import json

class ClusterView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )
    
    def list_brokers(self, request, bootstrap_server):
        clusterMeta = ClusterMetadata(bootstrap_servers=[bootstrap_server])
        brokerList = []
        for broker in clusterMeta.brokers():
            brokerList.append(broker.nodeId) 
        return JsonResponse(json.dumps(brokerList), safe=False)