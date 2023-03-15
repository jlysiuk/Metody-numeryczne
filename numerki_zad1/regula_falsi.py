from typing import Tuple, Any


def falsi_tolerance(f, a, b, d, count=0) -> int | tuple[Any, int | Any]:
    """
    wyznacza miejsce zerowe funkcji za pomocą Regula falsi
    :param f: wzór funkcji
    :param a: dolna granica przedziału izolacji
    :param b: górna granica przedziału izolacji
    :param d: tolerancja
    :param count: licznik iteracji klauzuli while
    :return:
    """
    if f(a) * f(b) >= 0:
        print("You have not assumed right a and b")
        return -1

    c = a  # Initialize result

    while True:
        count = count + 1
        # szukamy miejsca zerowego fałszywej prostej
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        # sprawdzamy czy x0 fałszywej prostej to x0 funkcji
        if abs(f(c)) < d:
            return c, count

        # wybieramy jedną połowę przedziału aby kontynuować
        elif (f(c) * f(a)) < 0:
            b = c

        else:
            a = c


# def falsi_iteration(f, a: float, b: float, i: int) -> float:
#     """
#     :param f:
#     :param a:
#     :param b:
#     :param i:
#     :return:
#     """

