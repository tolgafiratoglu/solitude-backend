from rest_framework import viewsets

from solitude.services.kafkaservice import KafkaService
from solitude.services.kafkaadminservice import KafkaAdminService
from solitude.services.clusterservice import ClusterService

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest

from django.forms.models import model_to_dict

from rest_framework.decorators import action

class TopicView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser, )
    authentication_classes = (JWTAuthentication, )

    def get_topic(self, request, cluster_id, topic):
        bootstrap_servers = ClusterService.get_cluster_brokers(cluster_id)
        partitions = KafkaService.get_topic_partitions(topic=topic, bootstrap_servers=bootstrap_servers)
        
        return JsonResponse({"status": "success", "num_partitions": len(partitions)})

    def save(self, request, cluster_id):
        topic_title = request.POST.get('topic_title', '')
        topic_partition = int(request.POST.get('topic_partition_number', ''))
        topic_replication_factor =int(request.POST.get('topic_replication_factor', ''))
        if topic_title == '' or topic_partition == 0 or topic_replication_factor == 0:
            return HttpResponseBadRequest(JsonResponse({"status": "error", "message": "Please provide valid values"}))
        bootstrap_servers = ClusterService.get_cluster_brokers(cluster_id)
        if bootstrap_servers is not None:
            try:
                KafkaAdminService.create_topic(bootstrap_servers, topic_title=topic_title, partition_number=topic_partition, replication_factor=topic_replication_factor)
                return JsonResponse({'status': 'success'})
            except Exception as e:
                return HttpResponseBadRequest(JsonResponse({'status': 'error', 'message': str(e)}))
        return JsonResponse({'status': 'error', 'message': "Cluster doesn't have any broker"})

    def create_partials(self, request, cluster_id, topic):
        bootstrap_servers = ClusterService.get_cluster_brokers(cluster_id)
        number_of_partitions = request.POST.get('number_of_partitions')
        try:
            KafkaAdminService.create_partitions(bootstrap_servers=bootstrap_servers, topic=topic, number_of_new_partitions=number_of_partitions)
            return JsonResponse({'status': 'success', 'message': number_of_partitions + ' partitions saved on topic: ' + topic})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})