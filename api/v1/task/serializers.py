from rest_framework import serializers

from api.v1.task.utils import get_messages
from api.v1.user.serializers import CustomUserShortSerializer
from task.models import Message
from task.tasks import send_message


class MessageCreateUpdateSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = Message
        fields = [
            'id',
            'subject',
            'content',
            'shipping_time',
            'receiver',
            'created_at',
            'is_active',
        ]
        extra_kwargs = {
            'receiver': {'required': True}
        }

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['receiver'] = CustomUserShortSerializer(instance.receiver).data
        return context


class MessageListSerializer(serializers.ModelSerializer):
    receiver = CustomUserShortSerializer()

    class Meta:
        model = Message
        fields = [
            'id',
            'subject',
            'content',
            'shipping_time',
            'receiver',
            'created_at',
        ]



class MessageDetailSerializer(serializers.ModelSerializer):
    receiver = CustomUserShortSerializer()

    class Meta:
        model = Message
        fields = [
            'id',
            'subject',
            'content',
            'shipping_time',
            'receiver',
            'created_at',
            'updated_at',
            'is_active',
        ]