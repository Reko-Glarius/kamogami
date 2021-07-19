from datetime import datetime
from typing import List, Optional, Union

import arrow
from arrow.arrow import Arrow
from django.db.models.query import QuerySet

from calendario.services import get_horario
from kamogami.constants import STATUS_SCHEDULED
from reservas.models import reserva, servicio
from usuarios.models import User


def get_reservas(fecha: Union[datetime.datetime, str]) -> QuerySet:
    """Obtener reservas para el dia 'fecha'"""
    return reserva.objects.filter(date__date=fecha)


def _reservar_hora(
    fecha: Union[datetime.datetime, str], servicio: servicio, user: User
) -> reserva:
    """Reserva una hora, OJO, no revisa si está disponible o no."""
    fecha = arrow.get(fecha)
    return reserva.objects.create(
        user=user,
        servicio=servicio,
        start_hour=fecha.time(),
        end_hour=fecha.shift(minutes=servicio.time_slots * 30).time(),
        date=fecha.date(),
        status=STATUS_SCHEDULED,
    )


def _time_slot_builder(
    inicio: Union[datetime.time, Arrow], termino: datetime.time, step: int = 30
) -> List[datetime.time]:
    """Helper para construir una lista de HH:mm con un step predefinido."""
    inicio = arrow.get(inicio)
    lista = []
    while inicio.datetime < termino:
        lista.append(inicio.time())
        inicio.shift(minutes=step)

    return lista


def get_horas_en_dia(fecha: Union[datetime.datetime, str]) -> List[datetime.time]:
    """Retorna una lista de tiempos en el horario disponible para 'fecha'."""
    horario = get_horario(fecha=fecha)
    inicio = arrow.get(horario.start_time)
    termino = horario.end_time
    return _time_slot_builder(inicio=inicio, termino=termino)


def get_horas_disponibles(fecha: Union[datetime.datetime, str]) -> List[datetime.time]:
    """Remueve las horas ocupadas en reservas para 'fecha'."""
    lista = get_horas_en_dia(fecha=fecha)
    reservas = get_reservas(fecha=fecha)
    for reserva in reservas:  # not very efficient :)
        for i in range(len(lista)):
            if reserva.start_hour <= lista[i] <= reserva.end_hour:
                lista.pop(i)
    return lista


def get_horas_por_servicio(
    fecha: Union[datetime.datetime, str], servicio: servicio
) -> List[datetime.time]:
    """Obtiene la disponibilidad de horas por un servicio de X time_slots."""
    horas = get_horas_disponibles(fecha=fecha)
    if len(horas) == 0:
        return horas
    time_slots = servicio.time_slots
    if time_slots == 1:
        return horas

    set_horas = set(horas)
    comienzo_servicio = horas[0]
    fin_servcio = arrow.get(horas[0]).shift(minutes=time_slots * 30)

    tiempo_servicio = set(
        _time_slot_builder(inicio=comienzo_servicio, termino=fin_servcio)
    )

    result = []
    for hora in horas:
        if tiempo_servicio.issubset(set_horas):
            result.append(hora)
        tiempo_servicio = {
            arrow.get(hora).shift(minutes=30).time() for hora in tiempo_servicio
        }

    return result
