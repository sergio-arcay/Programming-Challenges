"""
Reto #45

CONTENEDOR DE AGUA

    Fecha publicación enunciado: 07/10/22
    Fecha publicación resolución: 14/11/22

    Dificultad: MEDIA

    Enunciado: Dado un array de números enteros positivos, donde cada uno representa unidades
    de bloques apilados, debemos calcular cuantas unidades de agua quedarán atrapadas entre ellos.

        - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].

               ⏹
          ⏹💧💧⏹
          ⏹💧⏹⏹💧⏹
          ⏹💧⏹⏹💧⏹
          ⏹💧⏹⏹⏹⏹

        - Representando bloque con ⏹︎y agua con 💧, quedarán atrapadas 7 unidades de agua.

        - Suponemos que existe un suelo impermeable en la parte inferior que retiene el agua.


    Información adicional:

        - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
          para preguntas, dudas o prestar ayuda a la comunidad.

        - Tienes toda la información sobre los retos semanales en
          https://retosdeprogramacion.com/semanales2022.

"""

from time import time


def terminal_view(blocks, title="TABLE:"):

    # Calculate the amount of rows and columns
    Mrow, Mcol = max(blocks), len(blocks)

    # Initial table with a gup in the position of the every possible solid block
    table = [[" " for _ in range(Mcol)] for _ in range(Mrow)]

    # Set circles (zeros) in every filled block, according to the challenge input list
    for col, col_Mrow in enumerate(blocks):
        for row in range(Mrow - col_Mrow, Mrow):
            table[row][col] = "0"

    # Print the table vertically
    print("{}\n|{}|\n".format(
        title,
        '|\n|'.join(['|'.join(['   {:4}'.format(item) for item in row]) for row in table])
    ))


def challenge45_v1(blocks):
    t0 = time()

    # Calculate the RESULT for the challenge:
    #
    #       This line iterates over every block (left->right). Each block detects how many gaps exist on its right,
    #       until finding another block at higher or equal height. Each detected gap is equivalent to a potential water
    #       space.
    #
    #       This iteration with the first column would be:
    #
    #           |O|---- --->|0|   | |
    #           |O|-->|0|   |0|   |0|    =>  1 + 0 + 0 = 1 (One gap on the right-hand side of the whole first column)
    #           |O|-->|0|   |0|   |0|
    #
    result = sum(next((ncol - col - 1 for ncol, nMrow in list(enumerate(blocks))[col + 1:] if nMrow >= row), 0)
                 for col, Mrow in enumerate(blocks) for row in range(Mrow, 0, -1))

    return result, time() - t0


if __name__ == '__main__':

    inputs = {
        "test_1": [4, 0, 3, 3, 1, 3],  # 7
        "test_2": [1, 3, 2, 5, 0, 7],  # 6
    }

    average_time = -1

    for k, v in inputs.items():
        test_result, test_time = challenge45_v1(v)
        terminal_view(v, title=">> {} ---> R={} (t={})".format(k, test_result, test_time))
        average_time = ((average_time + test_time) / 2.0) if average_time >= 0 else test_time

    print("\n AVERAGE TIME --- {}".format(average_time))
