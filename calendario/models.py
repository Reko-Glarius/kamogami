from django.db import models

days_name=[
    ('L', 'Lunes'),
    ('M', 'Martes'),
    ('X', 'Miercoles'),
    ('J', 'Jueves'),
    ('V', 'Viernes'),
    ('S', 'Sabado'),
    ('D', 'Domingo'),
]
class attention_hours(models.Model):

    day = models.CharField(max_length=2,choices=days_name)
    start_time = models.TimeField(null=True, default=None)
    end_time = models.TimeField(null=True, default=None)
    valid_from = models.DateField(null=True, default=None)
    valid_until = models.DateField(default=None, null=True)
