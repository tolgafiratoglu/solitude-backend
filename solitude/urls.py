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

from solitude.views.topicview import TopicView
from solitude.views.brokerview import BrokerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cluster/<int:cluster_id>/brokers', BrokerView.as_view({'get': 'list_brokers'}), name='cluster_broker_list'),
    path('cluster/<int:cluster_id>/topics', BrokerView.as_view({'get': 'list_topics'}), name='cluster_topic_list'),
    path('cluster/<int:cluster_id>/consumers', BrokerView.as_view({'get': 'list_consumers'}), name='cluster_consumer_list'),
    path('broker/<int:broker_id>/topic/new', BrokerView.as_view({'get': 'new_topic'}), name='cluster_consumer_list'),
    path('topic/<int:topic_id>/partitions', BrokerView.as_view({'get': 'new_partition'}), name='topic_partition_list'),
]
