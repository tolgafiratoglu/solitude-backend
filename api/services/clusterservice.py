from api.models.brokermodel import Broker

class ClusterService():

    @classmethod
    def get_cluster_brokers(self, cluster_id):
        brokers = Broker.objects.filter(active=True).filter(cluster_id=cluster_id).all()
        broker_list = []
        for broker in brokers:
            broker_list.append(broker.host + ':' + str(broker.port))
        return broker_list    
