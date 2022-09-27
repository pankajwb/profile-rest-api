from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """return lists of features"""
        an_apiview = [
            'uses methods as functions',
            'is similar to default django view',
            'gives you most control over app logic',
            'is mapped manually to urls',
        ]

        return Response({'message':'Hello!', 'an_apiview' : an_apiview})
