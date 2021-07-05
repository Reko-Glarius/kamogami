from django.db import models


class attention_hours(models.Model):
    day = models.DateField()
    start_time = models.TimeField(null=True, default=None)
    end_time = models.TimeField(null=True, default=None)
    valid_from = models.DateField(null=True, default=None)
    valid_until = models.DateField(default=None, null=True)
