from django.test import TestCase

from api.serializers.clusterserializer import ClusterSerializer

from api.models.clustermodel import Cluster
from django.contrib.auth.models import User
from django.test import Client

import os

# Create your tests here.
class ClusterSerializerFunctionalTest(TestCase):
    def setUp(self):
        # Prepare cluster:
        test_user = User.objects.create_user(username='admin', email='admin@admin.com', password='admin')
        
    def test_cluster_serializer(self):
        c = Client()
        response = c.get('api/token/', {'username': 'admin', 'password': 'admin'})