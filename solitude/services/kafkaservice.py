from django.http import HttpResponse, JsonResponse

import kafka

class KafkaService():

    def get_consumer():
        return kafka.KafkaConsumer(
            bootstrap_servers=['localhost:9092'],
            client_id="python-test-consumer"
        )
        
    def get_topics(self):
        kafka_consumer = self.get_consumer()
        return JsonResponse(kafka_consumer.topics())