from rest_framework import viewsets
from solitude.serializers.brokerserializer import BrokerSerializer

from django.http import HttpResponse
from django.template import loader
from solitude.services.kafkaadminservice import KafkaAdminService
from solitude.services.kafkaservice import KafkaService
from django.shortcuts import redirect
from django.contrib import messages

class BrokerView(viewsets.ViewSet):

    def list_topics(self, request, host, port):
        bootstrap_server = host + ':' + str(port)
        topics = KafkaService.get_topics(bootstrap_server)
        context = {
            'topics': topics
        }
        template = loader.get_template('topic_list.html')
        return HttpResponse(template.render(context, request)) 

    def create_topic(self, request, host, port):
        context = {
            'host': host,
            'port': port,
            'partition_range': range(1, 20),
            'replication_range': range(1, 20)  
        }
        template = loader.get_template('create_update_topic.html')
        return HttpResponse(template.render(context, request))  

    def save_topic(self, request, host, port):
        broker_url = host + ':' + str(port)
        topic_title = request.POST.get('topic_title')
        topic_partition = int(request.POST.get('topic_partition_number'))
        topic_replication_factor = int(request.POST.get('topic_replication_factor'))
        try:
            KafkaAdminService.create_topic(broker_url, topic_title=topic_title, partition_number=topic_partition, replication_factor=topic_replication_factor)
            messages.add_message(request, messages.SUCCESS, 'Topic saved to host: '+broker_url)
            return redirect('/broker/'+host+'/'+str(port)+'/topics')
        except Exception as e:
            messages.add_message(request, messages.ERROR, str(e))        
            return redirect('/broker/'+host+'/'+str(port)+'/topic/new')