from rest_framework import viewsets
from solitude.serializers.brokerserializer import BrokerSerializer

from django.http import HttpResponse, JsonResponse
from solitude.services.kafkaadminservice import KafkaAdminService
from solitude.services.kafkaservice import KafkaService
from django.shortcuts import redirect

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class BrokerView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )

    def list_topics(self, request, bootstrap_server):
        topics = KafkaService.get_topics(bootstrap_server)
        return JsonResponse(topics, safe=False)

    def save_topic(self, request, bootstrap_server):
        topic_title = request.POST.get('topic_title')
        topic_partition = int(request.POST.get('topic_partition_number'))
        topic_replication_factor = int(request.POST.get('topic_replication_factor'))
        try:
            KafkaAdminService.create_topic(bootstrap_server, topic_title=topic_title, partition_number=topic_partition, replication_factor=topic_replication_factor)
            return redirect('/broker/'+bootstrap_server+'/topics')
        except Exception as e:
            return redirect('/broker/'+bootstrap_server+'/topic/new')