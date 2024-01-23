from rest_framework import serializers

from .models import Newsletter


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ["email"]

    def create(self, validated_data):
        email = validated_data.get("email")
        if Newsletter.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                detail="email already subscribed")
        return super().create(validated_data)


class MessageSerializer(serializers.Serializer):
    detail = serializers.CharField()
