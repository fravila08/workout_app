from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT,
)
from rest_framework.authtoken.models import Token
from .models import User

# Create your views here.
class Register(APIView):
    def post(self, request):
        try:
            new_user = User.objects.create_user(**request.data)
            token = Token.objects.create(user = new_user)
            login(request, new_user)
            return Response({"greeting": f"Welcome {new_user.username}!", "token": token.key})
        except Exception as e:
            print(e)
            return Response("Bad request", status=HTTP_400_BAD_REQUEST)
