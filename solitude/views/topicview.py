from rest_framework import generics, viewsets, status
from django.http import HttpResponse

import kafka
from kafka.admin import KafkaAdminClient, NewTopic

class TopicView(viewsets.ViewSet):

    def list(self, request, server_id):
        kafka_consumer = kafka.KafkaConsumer(
            bootstrap_servers=['localhost:9092'],
            client_id="python-test-consumer"
        )
        return HttpResponse(server_id)
