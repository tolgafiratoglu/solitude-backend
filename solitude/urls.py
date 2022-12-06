"""solitude URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from solitude.views.clusterview import ClusterView
from solitude.views.topicview import TopicView
from solitude.views.userview import UserView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
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