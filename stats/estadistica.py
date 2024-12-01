
import random
from math import ceil

def comprobar_cotizaciones(cotizacion_a, cotizacion_b, maximo):
    """
    Verifica si es posible realizar una sure bet y calcula las cantidades a apostar.

    :param cotizacion_a: Cotización de la casa A.
    :param cotizacion_b: Cotización de la casa B.
    :param maximo: Monto máximo a apostar.
    :return: Lista con resultados [bool, apuesta_a, apuesta_b].
    """
    try:
        a = float(cotizacion_a.replace(",", "."))
        b = float(cotizacion_b.replace(",", "."))
        valor_sure_bet = (1/a) + (1/b)
        
        if valor_sure_bet < 1:
            porcentaje_a = 1/a / valor_sure_bet
            porcentaje_b = 1/b / valor_sure_bet
            apuesta_a = ceil(porcentaje_b * maximo)
            apuesta_b = ceil(porcentaje_a * maximo)
            return [True, apuesta_a, apuesta_b]
        else:
            return [False, 0, 0]
    except ValueError as e:
        print(f"Error en comprobar_cotizaciones: {e}")
        return [False, 0, 0]

def calcular_ganancia(cotizacion_a, cotizacion_b, apuesta_a, apuesta_b):
    """
    Calcula las ganancias esperadas de una sure bet.

    :param cotizacion_a: Cotización de la casa A.
    :param cotizacion_b: Cotización de la casa B.
    :param apuesta_a: Monto apostado en la casa A.
    :param apuesta_b: Monto apostado en la casa B.
    :return: Porcentaje de ganancia esperada.
    """
    try:
        ganancia_a = cotizacion_a * apuesta_a
        ganancia_b = cotizacion_b * apuesta_b
        ganancia = max(ganancia_a, ganancia_b)
        total_apostado = apuesta_a + apuesta_b
        return (ganancia - total_apostado) / total_apostado * 100
    except ZeroDivisionError:
        return 0
