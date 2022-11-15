"""
Reto #46

¿DÓNDE ESTÁ EL ROBOT?

    Fecha publicación enunciado: 14/10/22
    Fecha publicación resolución: 21/11/22

    Dificultad: MEDIA

    Enunciado: Calcula dónde estará un robot (sus coordenadas finales) que se encuentra en una cudrícula
    representada por los ejes "x" e "y".

        - El robot comienza en la coordenada (0, 0).

        - Para indicarle que se mueva, le enviamos un array formado por enteros (positivos o negativos) que indican la
          secuencia de pasos a dar.

        - Por ejemplo: [10, 5, -2] indica que primero se mueve 10 pasos, se detiene, luego 5, se detiene, y
          finalmente 2. El resultado en este caso sería (x: -5, y: 12).

        - Si el número de pasos es negativo, se desplazaría en sentido contrario al que está mirando.

        - Los primeros pasos los hace en el eje "y". Interpretamos que está mirando hacia la parte
          positiva del eje "y".

        - El robot tiene un fallo en su programación: cada vez que finaliza una secuencia de pasos gira
          90 grados en el sentido contrario a las agujas del reloj.

    Información adicional:

        - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
          para preguntas, dudas o prestar ayuda a la comunidad.

        - Tienes toda la información sobre los retos semanales en
          https://retosdeprogramacion.com/semanales2022.

"""
import math


class Robot:
    def __init__(self, home_position=(0, 0), home_angle=math.pi / 2):
        self._home = (home_position, home_angle)
        self.position = home_position
        self.view_angle = home_angle

    def move(self, steps):
        self.position = (
            round(self.position[0] + steps * math.cos(self.view_angle), 2),
            round(self.position[1] + steps * math.sin(self.view_angle), 2)
        )
        self.rotate(math.pi / 2)

    def travel(self, route):
        for steps in route:
            self.move(steps)

    def rotate(self, angle):
        self.view_angle = (t - 2*math.pi) if (t := self.view_angle + angle) >= (2*math.pi) else t

    def home(self):
        self.position, self.view_angle = self._home


if __name__ == '__main__':

    inputs = {
        "test_1": [10, 5, -2],  # (-5.0, 12.0)
        "test_2": [2, -4, 0, 8, -8],  # (12.0, -6.0)
    }

    robot = Robot()

    for k, v in inputs.items():
        robot.travel(v)
        print("{}: {}".format(k, robot.position))
        robot.home()
