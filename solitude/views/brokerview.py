from rest_framework import viewsets

from django.http import JsonResponse
from solitude.services.kafkaadminservice import KafkaAdminService
from solitude.services.kafkaservice import KafkaService

from solitude.services.brokerservice import BrokerService

from django.shortcuts import redirect

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class BrokerView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )

    def list_topics(self, request, broker_id):
        broker_host = BrokerService.get_broker_url(broker_id)
        topics = KafkaService.get_topics(broker_host)
        return JsonResponse(topics, safe=False)
       
    def save_topic(self, request, broker_id):
        topic_title = request.POST.get('topic_title')
        topic_partition = int(request.POST.get('topic_partition_number'))
        topic_replication_factor = int(request.POST.get('topic_replication_factor'))
        broker_host = BrokerService.get_broker_url(broker_id)
        if broker_host is not None:
            try:
                KafkaAdminService.create_topic(broker_host, topic_title=topic_title, partition_number=topic_partition, replication_factor=topic_replication_factor)
                return JsonResponse({'status': 'success'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})
        else:       
            return JsonResponse({'status': 'error', 'message': "Broker doesn't have a valid host"})