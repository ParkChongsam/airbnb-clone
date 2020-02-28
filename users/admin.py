from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models  
#현재의 파일과 같은 폴더에 있는 models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields":(
                    "avatar",
                    "gender",
                    "bio",
                    "language",
                    "currency",
                    "superhost",
                )
            }
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )

    # list_display = ("username", "superhost", "currency", "language", "gender")
    # list_filter = ("superhost", "currency", "language")