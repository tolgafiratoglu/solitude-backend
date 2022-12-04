from solitude.models.brokermodel import Broker
from solitude.services.kafkaservice import KafkaService

from django.forms.models import model_to_dict

class BrokerService():

    def get_broker_by_id(cluster_id):
        return Broker.objects.filter(cluster_id=cluster_id).first()

    @classmethod
    def get_broker_servers(self, cluster_id):
        broker = self.get_broker_by_id(cluster_id)
        if broker is not None:
            return broker.host + ':' + str(broker.port)
        return ''

    @classmethod
    def get_cluster_brokers(self, cluster_id):
        brokers = Broker.objects.filter(active=True).filter(cluster_id=cluster_id).all()
        broker_list = []
        for broker in brokers:
            server = broker.host + ':' + str(broker.port)
            broker_obj = model_to_dict(broker)
            broker_obj['topics'] = KafkaService.get_topics(server)
            broker_list.append(broker_obj)
        return broker_list