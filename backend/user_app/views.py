from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from rest_framework.authtoken.models import Token
from .models import User


def log_in_user(request, user):
    token = Token.objects.create(user=user)
    login(request, user)
    return {"user": user.username, "token": token.key}


# Create your views here.
class Register(APIView):
    def post(self, request):
        try:
            new_user = User.objects.create_user(**request.data)
            response = log_in_user(request, new_user)
            return Response(
                response,
                status=HTTP_201_CREATED,
            )
        except Exception as e:
            print(e)
            return Response("Bad request", status=HTTP_400_BAD_REQUEST)


class Log_in(APIView):
    def post(self, request):
        try:
            user = authenticate(
                username=request.data.get("username"),
                password=request.data.get("password"),
            )
            print(user)
            if user:
                response = log_in_user(request, user)
                return Response(response, status=HTTP_200_OK)
            return Response("Invalid Credentials", status=HTTP_401_UNAUTHORIZED)
        except Exception as e:
            print(e)
            return Response(
                "Something went wrong", status=HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserPermissions(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class Actions(UserPermissions):
    def get(self, request):
        return Response(
            {
                "user": {
                    "email": request.user.email,
                    "username": request.user.username,
                    "date_joined": request.user.date_joined,
                }
            }
        )

    def put(self, request):
        try:
            new_username = request.data.get("new_username", request.user.username)
            new_password = request.data.get("new_password")
            password = request.data.get("password")
            password_confirmation = request.user.check_password(password)
            if password_confirmation:
                request.user.username = new_username
                if new_password:
                    request.user.set_password(new_password)
                request.user.save()
                return Response("User information has been updated successfully!")
            return Response("Bad Request", HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response("Error", status=HTTP_500_INTERNAL_SERVER_ERROR)


class Log_out(UserPermissions):
    def post(self, request):
        try:
            request.user.auth_token.delete()
            logout(request)
            return Response("You've logged out please sign in to get a new token")
        except Exception as e:
            print(e)
            return Response("Bad Request", status=HTTP_400_BAD_REQUEST)
