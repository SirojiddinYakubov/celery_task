from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied

from api.v1 import permissions
from . import serializers

User = get_user_model()


class UserListView(generics.ListAPIView):
    """ Список пользователей """
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.CustomUserShortSerializer
    permission_classes = [permissions.AllowAllPermission]


class UserCreateView(generics.CreateAPIView):
    """ Создать пользователь """
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.CustomUserCreateUpdateSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AdminPermission
    ]

class UserUpdateView(generics.UpdateAPIView):
    """ Редактировать пользователя """
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.CustomUserCreateUpdateSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AdminPermission
    ]

class AdminCreateView(generics.CreateAPIView):
    """ Создать админ """
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.AdminCreateUpdateSerializer
    permission_classes = [permissions.AdminPermission]

class AdminUpdateView(generics.UpdateAPIView):
    """ Редактировать админ """
    queryset = User.objects.filter(is_active=True, role=User.Role.ADMIN)
    serializer_class = serializers.AdminCreateUpdateSerializer
    permission_classes = [permissions.AdminPermission]



class UserDetailView(generics.RetrieveAPIView):
    """ О пользователе подробно """
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.CustomUserDetailSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AdminPermission
    ]

    def get_object(self):
        if self.request.user.role == User.Role.USER:
            if self.kwargs.get('pk') != self.request.user.id:
                raise PermissionDenied({"message": "You don't have permission to access",
                                        "object_id": self.kwargs.get('pk')})
        return super().get_object()


class UserDeleteView(generics.DestroyAPIView):
    """ Удалить пользователя """
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.CustomUserShortSerializer
    permission_classes = [permissions.AdminPermission]
