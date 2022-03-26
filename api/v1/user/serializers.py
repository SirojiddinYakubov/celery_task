from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class CustomUserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'email',
        ]


class CustomUserCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'is_superuser', 'is_staff')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'middle_name': {'required': True},
            'password': {'write_only': True},
            'last_login': {'read_only': True},
            'date_joined': {'read_only': True},
            'role': {'read_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
            validated_data['is_active'] = True
            validated_data.pop('password')
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['role'] = instance.get_role_display()
        return context


class AdminCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'is_superuser')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'middle_name': {'required': True},
            'password': {'write_only': True},
            'last_login': {'read_only': True},
            'date_joined': {'read_only': True},
            'role': {'read_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.role = User.Role.ADMIN
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
            validated_data.pop('password')
            validated_data['is_active'] = True
            validated_data['is_staff'] = True
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['role'] = instance.get_role_display()
        return context


class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'role',
            'last_login',
            'date_joined',
        ]

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['role'] = instance.get_role_display()
        return context
