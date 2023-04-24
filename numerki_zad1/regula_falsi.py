from typing import Tuple, Any

import horner


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
        print('wartości na początku i końcu przedziału są tych samych znaków. Wprowadź inne parametry.')
        aa = float(input('Podaj Parametr a: '))
        bb = float(input('Podaj Parametr b: '))
        falsi_tolerance(f, aa, bb, d)

    c = a

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


def falsi_tolerance_poly(tab, a, b, d, count = 0) -> int | tuple[Any, int | Any]:
    """
    wyznacza miejsce zerowe funkcji za pomocą Regula falsi
    :param tab: tablica współczynników wielomianu
    :param a: dolna granica przedziału izolacji
    :param b: górna granica przedziału izolacji
    :param d: tolerancja
    :param count: licznik iteracji klauzuli while
    :return:
    """
    if horner.horner_result(tab, a) * horner.horner_result(tab, b) >= 0:
        print('wartości na początku i końcu przedziału są tych samych znaków. Wprowadź inne parametry.')
        aa = float(input('Podaj Parametr a: '))
        bb = float(input('Podaj Parametr b: '))
        falsi_iteration_poly(tab, aa, bb, d)

    c = a  # Initialize result

    while True:
        count = count + 1
        # szukamy miejsca zerowego fałszywej prostej
        c = (a * horner.horner_result(tab, b) - b * horner.horner_result(tab, a)) / (
                    horner.horner_result(tab, b) - horner.horner_result(tab, a))

        # sprawdzamy czy x0 fałszywej prostej to x0 funkcji
        if abs(horner.horner_result(tab, c)) < d:
            return c, count

        # wybieramy jedną połowę przedziału aby kontynuować
        elif (horner.horner_result(tab, c) * horner.horner_result(tab, a)) < 0:
            b = c

        else:
            a = c


def falsi_iteration(f, a: float, b: float, i: int) -> float:
    """
    :param f: wzór funkcji
    :param a: dolna granica przedziału izolacji
    :param b: górna granica przedziału izolacji
    :param i: liczba iteracji
    :return:
    """
    if f(a) * f(b) >= 0:
        print('wartości na początku i końcu przedziału są tych samych znaków. Wprowadź inne parametry.')
        aa = float(input('Podaj Parametr a: '))
        bb = float(input('Podaj Parametr b: '))
        falsi_iteration(f, aa, bb, i)
    c = a
    for i in range(i):
        # szukamy miejsca zerowego fałszywej prostej
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        # wybieramy jedną połowę przedziału aby kontynuować
        if (f(c) * f(a)) < 0:
            b = c
        else:
            a = c
    return c


def falsi_iteration_poly(tab, a: float, b: float, i: int) -> float:
    """
    :param tab: tablica współczynników wielomianu
    :param a: dolna granica przedziału izolacji
    :param b: górna granica przedziału izolacji
    :param i: liczba iteracji
    :return:
    """
    if horner.horner_result(tab, a) * horner.horner_result(tab, b) >= 0:
        print('wartości na początku i końcu przedziału są tych samych znaków. Wprowadź inne parametry.')
        aa = float(input('Podaj Parametr a: '))
        bb = float(input('Podaj Parametr b: '))
        falsi_iteration_poly(tab, aa, bb, i)
    c = a
    for i in range(i):
        # szukamy miejsca zerowego fałszywej prostej
        c = (a * horner.horner_result(tab, b) - b * horner.horner_result(tab, a)) / (
                horner.horner_result(tab, b) - horner.horner_result(tab, a))
        # wybieramy jedną połowę przedziału aby kontynuować
        if (horner.horner_result(tab, c) * horner.horner_result(tab, a)) < 0:
            b = c
        else:
            a = c
    return c
