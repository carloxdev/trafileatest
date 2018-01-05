# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views import UserListAPIView


urlpatterns = [
    url(
        r'^users/$',
        UserListAPIView.as_view({'get': 'list'}),
        name="users-list"
    ),
]
