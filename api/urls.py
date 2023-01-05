from django.urls import path

from api.views.clusterview import ClusterView
from api.views.topicview import TopicView
from api.views.userview import UserView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/current-user', UserView.as_view({'get': 'current_user'}), name='current_user'),
    path('api/clusters', ClusterView.as_view({'get': 'list_clusters'}), name='cluster_list'),
    path('api/cluster/<int:cluster_id>', ClusterView.as_view({'get': 'get_info'}), name='get_cluster'),
    path('api/cluster/<int:cluster_id>/brokers', ClusterView.as_view({'get': 'list_brokers'}), name='cluster_broker_list'),
    path('api/cluster/<int:cluster_id>/topics', ClusterView.as_view({'get': 'list_topics'}), name='cluster_topic_list'),
    path('api/cluster/<int:cluster_id>/topic/save', TopicView.as_view({'post': 'save'}), name='save_topic'),
    path('api/cluster/<int:cluster_id>/topic/<str:topic>', TopicView.as_view({'get': 'get_topic'}), name='get_topic'),
    path('api/cluster/<int:cluster_id>/<str:topic>/partition/create', TopicView.as_view({'post': 'create_partials'}), name='create_partials'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]