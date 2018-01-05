# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Third-party Libraries
from import_export import resources
from import_export import fields
from import_export.admin import ImportExportModelAdmin

# Own's Libraries
# from .models import User


class UserResource(resources.ModelResource):

    class Meta:
        model = User
        exclude = ('id', )
        fields = (
            'username',
            'email',
            'date_joined',
            'last_login',
        )
        skip_unchanged = True
        import_id_fields = ['username', ]
        export_order = (
            'username',
            'email',
            'date_joined',
            'last_login',
        )


class CustomUserAdmin(ImportExportModelAdmin, UserAdmin):
    resource_class = UserResource
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
    )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
