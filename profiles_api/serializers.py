from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serialized a name field for testing"""
    name = serializers.CharField(max_length=10,min_length=3)   
