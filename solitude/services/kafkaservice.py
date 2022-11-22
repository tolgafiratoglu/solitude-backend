from django.http import HttpResponse, JsonResponse

import kafka

class KafkaService():

    def get_consumer(bootstrap_server):
        return kafka.KafkaConsumer(
            bootstrap_servers=[bootstrap_server],
            client_id="solitude-gui-consumer"
        )

    def get_topic_partitions(bootstrap_server, topic):
        consumer = kafka.KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_server
        )
        return consumer.partitions_for_topic(topic)
        
    @classmethod    
    def get_topics(self, bootstrap_server):
        kafka_consumer = self.get_consumer(bootstrap_server)
        topics = kafka_consumer.topics()
        topic_list = []
        for topic in topics:
            num_partitions = len(self.get_topic_partitions(bootstrap_server=bootstrap_server, topic=topic))
            topic_list.append({'topic': topic, 'num_partitions': num_partitions})
        return topic_list