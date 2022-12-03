from rest_framework import viewsets
from solitude.services.kafkaadminservice import KafkaAdminService
from solitude.services.brokerservice import BrokerService

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.http import JsonResponse

class TopicView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )

    def create_partials(self, request, broker_id, topic):
        host = BrokerService.get_broker_url(broker_id)
        number_of_partitions = request.POST.get('number_of_partitions')
        try:
            KafkaAdminService.create_partitions(host=host, topic=topic, number_of_new_partitions=number_of_partitions)
            return JsonResponse({'status': 'success', 'message': number_of_partitions + ' partitions saved on topic: ' + topic})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})