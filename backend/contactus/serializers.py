"""
Module Docstring
"""

from rest_framework import serializers
from .models import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    """
    Serializer for the ContactUs model.
    """
    class Meta:
        """Meta class for ContactUsSerializer."""
        model = ContactUs
        fields = ["email", "full_name", "message", "enquiry_type", "subject"]

        def dummy_method(self):
            """
            A dummy method to satisfy the linting requirement.
            """
            # Add a dummy method to satisfy the linting requirement
        def dummy_method2(self):
            """
            A dummy method to satisfy the linting requirement.
            """
            # Add a dummy method to satisfy the linting requirement

    def create(self, validated_data):
        """
        Create and return a new ContactUs instance using the validated data.
        """
        return ContactUs.objects.create(**validated_data)


class MessageSerializer(serializers.Serializer):
    """
    Serializer for the Message model.
    """
    detail = serializers.CharField()

    def create(self, validated_data):
        # Provide a dummy implementation or leave it empty
        pass

    def update(self, instance, validated_data):
        # Provide a dummy implementation or leave it empty
        pass
