from rest_framework import viewsets
from solitude.services.kafkaadminservice import KafkaAdminService
from solitude.services.brokerservice import BrokerService
from solitude.services.clusterservice import ClusterService

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.http import JsonResponse

class TopicView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser, )
    authentication_classes = (JWTAuthentication, )

    def save_topic(self, request, cluster_id):
        topic_title = request.POST.get('topic_title')
        topic_partition = int(request.POST.get('topic_partition_number'))
        topic_replication_factor = int(request.POST.get('topic_replication_factor'))
        bootstrap_servers = ClusterService.get_cluster_brokers(cluster_id)
        if bootstrap_servers is not None:
            try:
                KafkaAdminService.create_topic(bootstrap_servers, topic_title=topic_title, partition_number=topic_partition, replication_factor=topic_replication_factor)
                return JsonResponse({'status': 'success'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})
        else:       
            return JsonResponse({'status': 'error', 'message': "Broker doesn't have a valid host"})

    def create_partials(self, request, cluster_id, topic):
        bootstrap_servers = ClusterService.get_cluster_brokers(cluster_id)
        number_of_partitions = request.POST.get('number_of_partitions')
        try:
            KafkaAdminService.create_partitions(bootstrap_servers=bootstrap_servers, topic=topic, number_of_new_partitions=number_of_partitions)
            return JsonResponse({'status': 'success', 'message': number_of_partitions + ' partitions saved on topic: ' + topic})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})