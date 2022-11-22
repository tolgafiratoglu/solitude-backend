from kafka.admin import KafkaAdminClient, NewTopic

class KafkaAdminService():
    def create_topic(host, topic_title, partition_number, replication_factor):
        admin_client = KafkaAdminClient(bootstrap_servers=host, client_id='kafka-admin-client')
        topic_list = [NewTopic(name=topic_title, num_partitions=partition_number, replication_factor=replication_factor)]
        admin_client.create_topics(new_topics=topic_list, validate_only=False)