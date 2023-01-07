from django.db import models
from django.contrib.auth import get_user_model

from api.models import Cluster

class Broker(models.Model):
    managed = True
    created_by = models.ForeignKey(get_user_model(), unique=False, editable=False, on_delete=models.DO_NOTHING, default=None, blank=False, null=False)
    cluster = models.ForeignKey(Cluster, unique=False, editable=True, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    title = models.CharField(max_length=255, default='', null=False, blank=False)
    host = models.CharField(max_length=255, default='', null=False, blank=False)
    port = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    notes = models.TextField('Notes', default='', null=True, blank=True)
    
    class Meta:
        db_table = "solitude_brokers"