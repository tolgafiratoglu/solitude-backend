from rest_framework import viewsets
from django.http import HttpResponse

class ServerView(viewsets.ViewSet):

    def list(self, request):
        return HttpResponse('test')
