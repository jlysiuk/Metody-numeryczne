from typing import Tuple
import plotting
import numpy as np
from matplotlib import pyplot as plt
import horner


def bisection_tolerance(f, a: float, b: float, d: float, c=1) -> float | tuple[float, int]:
    """
    :param f: funkcja na której użyta będzie metoda bisekcji
    :param a: dolna granica przedziału izolacji
    :param b: górna granica przedziału izolacji
    :param d: dokładność
    :param c: licznik cykli rekurencji
    :return:
    """
    c = c + 1
    if np.sign(f(a)) == np.sign(f(b)):
        print('wartości na początku i końcu przedziału są tych samych znaków. Wprowadź inne parametry.')
        aa = float(input('Podaj Parametr a: '))
        bb = float(input('Podaj Parametr b: '))
        bisection_tolerance(f, aa, bb, d)

    # sprawdzenie, czy któryś z krańców przedziału nie jest miejscem zerowym
    if np.abs(f(a)) < d:
        return a, c

    if np.abs(f(b)) < d:
        return b, c

    # wyznaczanie środka przedziału
    x = (a + b) / 2

    # sprawdzenie, czy środek przedziału nie jest miejscem zerowym
    if np.abs(f(x)) < d:
        return x, c

    # sprawdzenie w której połowie przedziału wartości funkcji zmieniają znak
    if f(a) * f(x) < 0:
        return bisection_tolerance(f, a, x, d, c)
    else:
        return bisection_tolerance(f, x, b, d, c)


def bisection_tolerance_poly(tab, a: float, b: float, d: float, c=1) -> tuple[float, int] | float:
    """
    :param tab: tabela wspólczynników wielomianu
    :param a: dolna granica przedziału izolacji
    :param b: górna granica przedziału izolacji
    :param d: dokładność
    :param c: licznik cykli rekurencji
    :return:
    """
    c = c + 1
    aa = a
    bb = b
    if np.sign(horner.horner_result(tab, a)) == np.sign(horner.horner_result(tab, b)):
        print('wartości na początku i końcu przedziału są tych samych znaków. Wprowadź inne parametry.')
        aa = float(input('Podaj Parametr a: '))
        bb = float(input('Podaj Parametr b: '))
        bisection_tolerance_poly(tab, aa, bb, d)

    # sprawdzenie, czy któryś z krańców przedziału nie jest miejscem zerowym
    if np.abs(horner.horner_result(tab, a)) < d:
        return a, c

    if np.abs(horner.horner_result(tab, b)) < d:
        return b, c

    # wyznaczanie środka przedziału
    x = (a + b) / 2

    # sprawdzenie, czy środek przedziału nie jest miejscem zerowym
    if np.abs(horner.horner_result(tab, x)) < d:
        return x, c

    # sprawdzenie w której połowie przedziału wartości funkcji zmieniają znak
    if horner.horner_result(tab, a) * horner.horner_result(tab, x) < 0:
        return bisection_tolerance_poly(tab, a, x, d, c)
    else:
        return bisection_tolerance_poly(tab, x, b, d, c)


def bisection_iteration(f, a: float, b: float, i: int) -> float:
    """
    :param f: funkcja na której użyta będzie metoda bisekcji
    :param a: dolna granica przedziału izolacji
    :param b: górna granica przedziału izolacji
    :param i: liczba iteracji
    :return:
    """

    if np.sign(f(a)) == np.sign(f(b)):
        print('wartości na początku i końcu przedziału są tych samych znaków. Wprowadź inne parametry.')
        aa = float(input('Podaj Parametr a: '))
        bb = float(input('Podaj Parametr b: '))
        bisection_tolerance(f, aa, bb, i)

    for i in range(i):
        # wyznaczanie środka przedziału
        x = (a + b) / 2
        # sprawdzenie w której połowie przedziału wartości funkcji zmieniają znak
        if f(x) * f(a) < 0:
            b = x
        else:
            a = x
    return x


def bisection_iteration_poly(tab, a: float, b: float, i: int) -> float:
    """
    :param tab: tablica współczynników wielomianu
    :param a: dolna granica przedziału izolacji
    :param b: górna granica przedziału izolacji
    :param i: liczba iteracji
    :return:
    """
    if np.sign(horner.horner_result(tab, a)) == np.sign(horner.horner_result(tab, b)):
        print('wartości na początku i końcu przedziału są tych samych znaków. Wprowadź inne parametry.')
        aa = float(input('Podaj Parametr a: '))
        bb = float(input('Podaj Parametr b: '))
        bisection_tolerance(tab, aa, bb, i)

    for i in range(i):
        # wyznaczanie środka przedziału
        x = (a + b) / 2
        # sprawdzenie w której połowie przedziału wartości funkcji zmieniają znak
        if horner.horner_result(tab, x) * horner.horner_result(tab, a) < 0:
            b = x
        else:
            a = x
    return x
