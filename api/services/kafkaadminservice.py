from kafka.admin import KafkaAdminClient, NewTopic
from kafka.admin.new_partitions import NewPartitions

class KafkaAdminService():

    def get_admin_client(bootstrap_servers):
        return KafkaAdminClient(bootstrap_servers=bootstrap_servers, client_id='kafka-admin-client')

    @classmethod
    def create_topic(self, bootstrap_servers, topic_title, partition_number, replication_factor):
        admin_client = self.get_admin_client(bootstrap_servers)
        topic_list = [NewTopic(name=topic_title, num_partitions=partition_number, replication_factor=replication_factor)]
        admin_client.create_topics(new_topics=topic_list, validate_only=False)

    @classmethod
    def create_partitions(self, bootstrap_servers, topic, number_of_new_partitions):
        admin_client = self.get_admin_client(bootstrap_servers)
        return admin_client.create_partitions({
            topic : NewPartitions(int(number_of_new_partitions))
        })
        