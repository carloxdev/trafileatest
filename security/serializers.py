# -*- coding: utf-8 -*-

# Django's Libraries
from django.contrib.auth.models import User

# Third-party Libraries
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'date_joined',
            'last_login',
        )
