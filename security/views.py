# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django's Libraries
from django.contrib.auth.models import User

# Third-party Libraries
# from rest_framework import status
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# from rest_framework.response import Response

# Own's Libraries
from .serializers import UserSerializer


class UserListAPIView(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
