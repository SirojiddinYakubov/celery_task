from django.contrib.auth import get_user_model
from rest_framework import generics
from api.v1 import permissions
from task.models import Message
from . import serializers

User = get_user_model()


class MessageListView(generics.ListAPIView):
    """ Список сообщений """
    queryset = Message.objects.filter(is_active=True)
    serializer_class = serializers.MessageListSerializer
    permission_classes = [permissions.AdminPermission]


class MessageCreateView(generics.CreateAPIView):
    """ Создать сообщение """
    queryset = Message.objects.filter(is_active=True)
    serializer_class = serializers.MessageCreateUpdateSerializer
    permission_classes = [permissions.AdminPermission]


class MessageUpdateView(generics.UpdateAPIView):
    """ Редактировать сообщение """
    queryset = Message.objects.filter(is_active=True)
    serializer_class = serializers.MessageCreateUpdateSerializer
    permission_classes = [permissions.AdminPermission]


class MessageDetailView(generics.RetrieveAPIView):
    """ О сообщение подробно """
    queryset = Message.objects.filter(is_active=True)
    serializer_class = serializers.MessageDetailSerializer
    permission_classes = [permissions.AdminPermission]


class MessageDeleteView(generics.DestroyAPIView):
    """ Удалить сообщение """
    queryset = Message.objects.filter(is_active=True)
    serializer_class = serializers.MessageDetailSerializer
    permission_classes = [permissions.AdminPermission]
