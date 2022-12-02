from solitude.models.brokermodel import Broker

class BrokerService():

    def get_broker_by_id(broker_id):
        return Broker.objects.filter(id=broker_id).first()

    @classmethod
    def get_broker_url(self, broker_id):
        broker = self.get_broker_by_id(broker_id)
        if broker is not None:
            return broker.host + ':' + str(broker.port)
        return ''    