from django.contrib import admin
from django.db import models
from django.contrib.auth import get_user_model

class Cluster(models.Model):
    managed = True
    use_in_migrations = True
    created_by = models.ForeignKey(get_user_model(), unique=False, editable=True, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    title = models.CharField(max_length=255, default='', null=False, blank=False)
    bootstrap_server_host = models.CharField(max_length=255, default='', null=False, blank=False)
    bootstrap_server_port = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    notes = models.TextField('Notes', default='', null=True, blank=True)
    
    class Meta:
        db_table = "solitude_clusters"