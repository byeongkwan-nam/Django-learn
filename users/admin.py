from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User) # 내가 만든 User와의 연결고리
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom fields",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio"
                )
            }
        ),
    )