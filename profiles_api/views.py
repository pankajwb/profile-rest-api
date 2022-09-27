from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API view"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """return lists of features"""
        an_apiview = [
            'uses methods as functions',
            'is similar to default django view',
            'gives you most control over app logic',
            'is mapped manually to urls',
        ]

        return Response({'message':'Hello!', 'an_apiview' : an_apiview})

    def post(self, request):
        """create hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST   
            )

    def put(self, request, pk=None):
        """Handling update"""
        return Response({'message' : 'Method is Put'})

    def patch(self, request, pk=None):
        """Handling update"""
        return Response({'message' : 'Method is Patch'})

    def delete(self, request, pk=None):
        """Handling update"""
        return Response({'message' : 'Method is Delete'}) 


class HelloViewSet(viewsets.ViewSet):
    """Test api viewsets"""
    
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        a_viewset = [
          'user crud',
          'map urls',
          'more features with less code',  
        ]

        return Response({'Message' : 'Hello!', 'viewset' : a_viewset})

    def create(self, request):
        """new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """retrieve request"""
        return Response({'http-method' : 'GET'})

    def update(self, request, pk=None):
        """retrieve request"""
        return Response({'http-method' : 'PUT'})
    
    def partial_update(self, request, pk=None):
        """retrieve request"""
        return Response({'http-method' : 'Partial update PATCH'})

    def destroy(self, request, pk=None):
        """retrieve request"""
        return Response({'http-method' : 'DESTROY'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)

    permission_classes = (permissions.UpdateOwnProfile,)