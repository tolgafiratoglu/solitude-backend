from django.test import TestCase

from api.serializers.clusterserializer import ClusterSerializer

class ClusterSerializerUnitTest(TestCase):
    
    def test_cluster_serializer_unit_test(self):
        cluster_data = {'id': 1, 'title': 'test', 'notes': 'test note'}
        cluster_serializer = ClusterSerializer(cluster_data, many=False)
        if cluster_serializer.data:
            self.assertEqual(cluster_serializer.data.get("notes"), 'test note')