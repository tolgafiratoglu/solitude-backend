from rest_framework import viewsets
from django.http import HttpResponse
import kafka
from kafka.admin import KafkaAdminClient, NewTopic

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class TopicView(viewsets.ViewSet):

    @method_decorator(login_required(login_url='/login'))
    def list(self, request, server_id):
        kafka_consumer = kafka.KafkaConsumer(
            bootstrap_servers=['localhost:9092'],
            client_id="python-test-consumer"
        )
        return HttpResponse(server_id)
