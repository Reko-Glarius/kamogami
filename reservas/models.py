from django.db import models
from django.contrib.auth.models import User
from kamogami.constants import STATUS_CHOICES

class servicio(models.Model):
    time_slots = models.IntegerField() # 1 time slot = 30 mins
    name = models.CharField(max_length=100)
    description = models.TextField()
    reference_price = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.time_slots * 30} min"


class reserva(models.Model):
    servicio = models.OneToOneField(
         servicio,
         on_delete=models.DO_NOTHING,
         db_constraint=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    date = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)