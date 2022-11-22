from rest_framework import viewsets
from solitude.models.clustermodel import Cluster
from kafka.cluster import ClusterMetadata
from django.http import HttpResponse
from django.template import loader

class ClusterView(viewsets.ModelViewSet):
    
    def list_brokers(self, request, host, port):
        clusterMeta = ClusterMetadata(bootstrap_servers=[host+':'+str(port)])
        context = {
            'brokers' : clusterMeta.brokers()
        }    
        template = loader.get_template('broker_list.html')
        return HttpResponse(template.render(context, request))