from rest_framework import viewsets
from solitude.models.brokermodel import Broker
from django.http import JsonResponse

from django.forms.models import model_to_dict

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

import json

class ClusterView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )
    
    def list_brokers(self, request, cluster_id):
        brokers = Broker.objects.filter(cluster=cluster_id).filter(active=True).all()
        brokerList = []
        for broker in brokers:
            brokerList.append(model_to_dict(broker))
        return JsonResponse(brokerList, safe=False)