from rest_framework import viewsets
from solitude.services.kafkaadminservice import KafkaAdminService

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.http import JsonResponse

class TopicView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )

    def create_partials(self, request, topic):
        number_of_partials = request.POST.get('number_of_partials')
        try:
            KafkaAdminService.create_partial(topic=topic, number_of_new_partitions=number_of_partials)
            return JsonResponse({'status': 'success', 'message': number_of_partials + 'saved on topic: ' + topic})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})