from django.contrib import admin
from django.db import models
from django.contrib.auth import get_user_model

class Server(models.Model):
    managed = True
    created_by = models.ForeignKey(get_user_model(), unique=True, editable=False, on_delete=models.DO_NOTHING, default=None, blank=False, null=False)
    active = models.BooleanField(default=True)
    host = models.CharField(max_length=255, default='', null=False, blank=False)
    port = models.PositiveIntegerField()
    notes = models.TextField('Notes', default='', null=True, blank=True)
    
    class Meta:
        db_table = "solitude_servers"