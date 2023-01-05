from rest_framework import viewsets
from api.models.brokermodel import Broker
from api.models.clustermodel import Cluster
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse

from django.forms.models import model_to_dict
from django.db.models import Count

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.services.brokerservice import BrokerService

from api.services.clusterservice import ClusterService
from api.services.kafkaservice import KafkaService

from api.serializers.clusterserializer import ClusterSerializer

import json

class ClusterView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )
    
    def list_clusters(self, request):
        clusters = Cluster.objects.annotate(num_brokers=Count('broker')).filter(active=True).all()
        clusterList = []
        for cluster in clusters:
            cluster_obj = model_to_dict(cluster)
            cluster_obj['num_brokers'] = cluster.num_brokers
            cluster_obj['brokers'] = BrokerService.get_cluster_brokers(cluster.pk)
            clusterList.append(cluster_obj)
        return JsonResponse(clusterList, safe=False)

    def list_topics(self, request, cluster_id):
        broker_servers = ClusterService.get_cluster_brokers(cluster_id)
        topics = KafkaService.get_topics(broker_servers)
        return JsonResponse(topics, safe=False)    

    def list_brokers(self, request, cluster_id):
        brokers = Broker.objects.filter(cluster=cluster_id).filter(active=True).all()
        brokerList = []
        for broker in brokers:
            brokerList.append(model_to_dict(broker))
        return JsonResponse(brokerList, safe=False)

    def get_info(self, request, cluster_id):
        response_data = {'status': 'success', 'data': []}
        cluster_query = Cluster.objects.filter(id=cluster_id).filter(active=True).first()
        cluster_serializer = ClusterSerializer(cluster_query, many=False)
        if cluster_serializer.data is None:
            response_data["error"] = cluster_serializer.errors
            return HttpResponseBadRequest(json.dumps(response_data))    
        response_data['data'] = cluster_serializer.data    
        return HttpResponse(json.dumps(cluster_serializer.data))