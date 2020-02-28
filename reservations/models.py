from django.db import models
from core import models as core_models

class Reservation(core_models.TimeStampModel):
        """ Reservation model Definition """
        STATUS_PENNDING = "pending"
        STATUS_CONFIRMED = "confirmed"
        STATUS_CANCELED = "canceled"

        STATUS_CHOICES =(
                (STATUS_PENNDING, "Pending"),
                (STATUS_CONFIRMED, "Confirmed"),
                (STATUS_CANCELED, "Cancel"),
        )

        check_in = models.DateField()
        check_out = models.DateField()
        status = models.CharField(max_length=12, choices = STATUS_CHOICES)
        guest = models.ForeignKey("users.User", related_name = "reservations", on_delete=models.CASCADE)
        room = models.ForeignKey("rooms.Room", related_name = "reservations", on_delete=models.CASCADE)

        def __str__(self):
                return f"{self.room} - {self.check_in}"
