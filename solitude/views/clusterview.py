from rest_framework import viewsets
from solitude.models.brokermodel import Broker
from solitude.models.clustermodel import Cluster
from django.http import JsonResponse

from django.forms.models import model_to_dict
from django.db.models import Count

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from solitude.services.brokerservice import BrokerService

from solitude.services.clusterservice import ClusterService
from solitude.services.kafkaservice import KafkaService

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