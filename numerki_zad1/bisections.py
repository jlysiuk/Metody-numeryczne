import numpy as np

import horner


def bisection_tolerance(f, a: float, b: float, d: float) -> float:
    """
    :param f: funkcja na której użyta będzie metoda bisekcji
    :param a: dolna granica przedziału izolacji
    :param b: górna granica przedziału izolacji
    :param d: dokładność
    :return:
    """
    if np.sign(f(a)) == np.sign(f(b)):
        print('wartości na początku i końcu przedziału są tych samych znaków. Wprowadź inne parametry.')
        aa = float(input('Podaj Parametr a: '))
        bb = float(input('Podaj Parametr b: '))
        bisection_tolerance(f, aa, bb, d)

    # sprawdzenie, czy któryś z krańców przedziału nie jest miejscem zerowym
    if np.abs(f(a)) < d:
        return a

    if np.abs(f(b)) < d:
        return b

    # wyznaczanie środka przedziału
    x = (a + b) / 2

    # sprawdzenie, czy środek przedziału nie jest miejscem zerowym
    if np.abs(f(x)) < d:
        return x

    if f(a) * f(x) < 0:
        return bisection_tolerance(f, a, x, d)
    else:
        return bisection_tolerance(f, x, b, d)


def bisection_tolerance_poly(tab, a: float, b: float, d: float) -> float:
    """
    :param f: funkcja na której użyta będzie metoda bisekcji
    :param a: dolna granica przedziału izolacji
    :param b: górna granica przedziału izolacji
    :param d: dokładność
    :return:
    """
    if np.sign(horner.horner_result(tab, a)) == np.sign(horner.horner_result(tab, b)):
        print('wartości na początku i końcu przedziału są tych samych znaków. Wprowadź inne parametry.')
        aa = float(input('Podaj Parametr a: '))
        bb = float(input('Podaj Parametr b: '))
        bisection_tolerance_poly(tab, aa, bb, d)

    # sprawdzenie, czy któryś z krańców przedziału nie jest miejscem zerowym
    if np.abs(horner.horner_result(tab, a)) < d:
        return a

    if np.abs(horner.horner_result(tab, b)) < d:
        return b

    # wyznaczanie środka przedziału
    x = (a + b) / 2

    # sprawdzenie, czy środek przedziału nie jest miejscem zerowym
    if np.abs(horner.horner_result(tab, x)) < d:
        return x

    if horner.horner_result(tab, a) * horner.horner_result(tab, x) < 0:
        return bisection_tolerance_poly(tab, a, x, d)
    else:
        return bisection_tolerance_poly(tab, x, b, d)


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
        x = (a + b) / 2
        if f(a) * f(b) < 0:
            b = x
        else:
            a = x

    return x
