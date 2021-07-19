import datetime
from typing import Union

import arrow

from calendario.models import attention_hours


def day_map(dia: int) -> str:
    map = ["L", "M", "X", "J", "V", "S", "D"]
    return map[dia]


def get_horario_default(weekday: str) -> attention_hours:
    return attention_hours.objects.get(
        day=weekday,
        valid_from=None,
        valid_until=None,
    )


def get_horario(fecha: Union[str, datetime.date]) -> attention_hours:
    """ "Obtiene las horas de atencion para una fecha.

    Retorna el valor default si es que no encuentra una fecha con rango.
    """
    fecha = arrow.get(fecha)
    weekday = fecha.weekday()
    weekday = day_map(weekday)
    try:
        day = attention_hours.objects.get(
            day=weekday, valid_from__gte=fecha.datetime, valid_until__lte=fecha.datetime
        )
    except attention_hours.DoesNotExist:
        return get_horario_default(weekday=weekday)
    return day
