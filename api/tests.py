from django.test import TestCase

from api.serializers.clusterserializer import ClusterSerializer

from api.models.clustermodel import Cluster

# Create your tests here.
class SerializerTest(TestCase):

    def setUp(self):
        Cluster.objects.create(title="Test Cluster", notes="Cluster Notes")

    def test_cluster_serializer(self):
        cluster_query = Cluster.objects.filter(title="Test Cluster").filter(active=True).first()
        cluster_serializer = ClusterSerializer(cluster_query, many=False)
        self.assertEqual(cluster_serializer.data.get('title'), 'Test Cluster')