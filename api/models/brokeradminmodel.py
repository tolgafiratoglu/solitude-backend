from django.contrib import admin
from api.models.brokermodel import Broker

class BrokerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Broker, BrokerAdmin)