from django.test import TestCase

from api.models.clustermodel import Cluster
from django.contrib.auth.models import User
from django.test import Client

import os

# Create your tests here.
class ClusterListFunctionalTest(TestCase):
        
    def test_cluster_list_response(self):
        c = Client()
        response = c.get('/api/clusters')
        self.assertEqual(response.status_code, 401)