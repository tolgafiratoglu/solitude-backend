from django.contrib import admin
from api.models.clustermodel import Cluster

class ClusterAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Cluster, ClusterAdmin)