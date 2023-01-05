from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.http import HttpResponse, HttpResponseBadRequest

from django.contrib.auth.models import User
from api.serializers.currentuserserializer import CurrentUserSerializer

import json

class UserView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )

    def current_user(self, request):
        response_data = {"status": "error", "data": {}, "error": []}
        current_user_id = int(self.request.user.id)
        user_query = User.objects.filter(id=current_user_id).first()
        serializer_user = CurrentUserSerializer(user_query, many=False)
        if serializer_user.data is None:
            response_data["error"] = serializer_user.errors
            return HttpResponseBadRequest(json.dumps(response_data))
        response_data["status"] = True;    
        response_data["data"] = serializer_user.data    
        return HttpResponse(json.dumps(response_data))    