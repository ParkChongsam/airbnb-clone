from django.contrib import admin
from . import models

@admin.register(models.Reservation)
class Reservation(admin.ModelAdmin):
        """ Reservation Admin Definition """
        list_display = (
                "room",
                "status",
                "check_in",
                "check_out",
        )

