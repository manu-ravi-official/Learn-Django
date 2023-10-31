from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from eventwire.error_codes import ERROR_NAME_NOT_FOUND
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import Group

from .roles import UserRoles
from .serializers import UserSerializer
from django.contrib.auth.decorators import permission_required


class CustomModeratorCreate(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if 'first_name' not in request.data:
            error_response = ERROR_NAME_NOT_FOUND
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            # Create the user
            encoded_password = make_password(request.data.get('password'))
            serializer.validated_data['password'] = encoded_password
            role = UserRoles.MODERATOR.value  # Store the integer value
            serializer.validated_data['role'] = role
            serializer.save()
            response_data = {'message': 'User created successfully'}
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            error_response = serializer.errors
            return Response(list(error_response.values())[0], status=status.HTTP_400_BAD_REQUEST)


class CustomUserCreate(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if 'first_name' not in request.data:
            error_response = ERROR_NAME_NOT_FOUND
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            # Create the user
            encoded_password = make_password(request.data.get('password'))
            serializer.validated_data['password'] = encoded_password
            role = UserRoles.USER.value  # Store the integer value
            serializer.validated_data['role'] = role
            serializer.save()
            response_data = {'message': 'User created successfully'}
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            error_response = serializer.errors
            return Response(list(error_response.values())[0], status=status.HTTP_400_BAD_REQUEST)


class CustomEmployeeCreate(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if 'first_name' not in request.data:
            error_response = ERROR_NAME_NOT_FOUND
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            # Create the user
            encoded_password = make_password(request.data.get('password'))
            serializer.validated_data['password'] = encoded_password
            role = UserRoles.EMPLOYEE.value  # Store the integer value
            serializer.validated_data['role'] = role
            serializer.save()
            response_data = {'message': 'User created successfully'}
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            error_response = serializer.errors
            return Response(list(error_response.values())[0], status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            # User is authenticated; generate access and refresh tokens
            refresh = RefreshToken.for_user(user)

            response_data = {
                'message': 'Login successful',
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            error_response = {'message': 'Invalid credentials'}
            return Response(error_response, status=status.HTTP_401_UNAUTHORIZED)
