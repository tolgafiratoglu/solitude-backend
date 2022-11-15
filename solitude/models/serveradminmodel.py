from django.contrib import admin
from solitude.models.servermodel import Server

class ServerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Server, ServerAdmin)