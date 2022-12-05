"""
Reto #48

¿Conoces el calendario de adviento de la comunidad (https://adviento.dev)? 24 días, 24 regalos sorpresa relacionados con
desarrollo de software, ciencia y tecnología desde el 1 de diciembre.

Crea una función que reciba un objeto de tipo "Date" y retorne lo siguiente:

    - Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo de ese día (a tu elección) y cuánto
    queda para que finalice el sorteo de ese día.

    - Si la fecha es anterior: Cuánto queda para que comience el calendario.

    - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.

Notas:

    - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00 y finaliza a las 23:59:59.

    - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos y segundos.

    - 🎁 Cada persona que aporte su solución entrará en un nuevo sorteo del calendario de aDEViento hasta el día de su
    corrección (sorteo exclusivo para quien entregue su solución).

------------------------------------------------------------------------------------------------------------------------

¡ALERTA!

Este código lo ha realizado chatGPT simplemente pasándole el reto. No tiene ningún sentido.

"""

from datetime import datetime


def calendario_adviento(fecha):
    # Fecha de inicio del calendario de adviento 2022
    inicio_adviento = datetime(2022, 12, 1)

    # Fecha de finalización del calendario de adviento 2022
    final_adviento = datetime(2022, 12, 24, 23, 59, 59)

    # Si la fecha recibida coincide con el calendario de adviento
    if inicio_adviento <= fecha <= final_adviento:
        # Calcular el número de día del calendario
        num_dia = (fecha - inicio_adviento).days + 1

        # Mostrar el regalo del día y cuánto queda para que finalice el sorteo
        print(f"Hoy es el día {num_dia} del calendario de adviento.")
        print(f"El regalo de hoy es un libro sobre programación en Python.")
        print(f"Quedan {final_adviento - fecha} para que finalice el sorteo.")

    # Si la fecha es anterior al calendario de adviento
    elif fecha < inicio_adviento:
        # Mostrar cuánto queda para que comience el calendario
        print(f"Quedan {inicio_adviento - fecha} para que comience el calendario de adviento.")

    # Si la fecha es posterior al calendario de adviento
    else:
        # Mostrar cuánto tiempo ha pasado desde que ha finalizado
        print(f"Han pasado {fecha - final_adviento} desde que finalizó el calendario de adviento.")


if __name__ == '__main__':

    # Crear una fecha de prueba (por ejemplo, el día 15 del calendario de adviento)
    fecha_prueba = datetime(2022, 12, 15, 12, 30, 0)

    # Llamar a la función con la fecha de prueba
    calendario_adviento(fecha_prueba)
