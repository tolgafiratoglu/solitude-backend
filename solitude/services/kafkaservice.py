from django.http import HttpResponse, JsonResponse

import kafka

class KafkaService():

    def get_consumer(bootstrap_servers):
        return kafka.KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            client_id="solitude-gui-consumer"
        )

    def get_topic_partitions(bootstrap_servers, topic):
        consumer = kafka.KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers
        )
        return consumer.partitions_for_topic(topic)
        
    @classmethod    
    def get_topics(self, bootstrap_servers):
        kafka_consumer = self.get_consumer(bootstrap_servers)
        topics = kafka_consumer.topics()
        topic_list = []
        for topic in topics:
            num_partitions = len(self.get_topic_partitions(bootstrap_servers=bootstrap_servers, topic=topic))
            topic_list.append({'topic': topic, 'num_partitions': num_partitions})
        return topic_list