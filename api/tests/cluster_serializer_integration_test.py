from django.test import TestCase

from api.serializers.clusterserializer import ClusterSerializer

from api.models.clustermodel import Cluster
from django.contrib.auth.models import User

# Create your tests here.
class ClusterSerializerIntegrationTest(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='test', email='test@test.com', password='test')
        Cluster.objects.create(title="Test Cluster", notes="Cluster Notes", created_by=test_user)
        
    def test_cluster_serializer(self):
        cluster_query = Cluster.objects.filter(title="Test Cluster").filter(active=True).first()
        cluster_serializer = ClusterSerializer(cluster_query, many=False)
        self.assertEqual(cluster_serializer.data.get('title'), 'Test Cluster')