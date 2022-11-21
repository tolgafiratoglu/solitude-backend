from solitude.models.clustermodel import Cluster

def cluster_context(request):
    context_data = dict()
    context_data['cluster_list'] = Cluster.objects.all()
    return context_data