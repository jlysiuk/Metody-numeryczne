import numpy as np
from matplotlib import pyplot as plt

import horner


def poly_y_for_plot(x, tab):
    # Funkcja zmieniająca tablicę współczynników w y przechowujący funkcję (do plot)
    """
    :param x: przedział x'ów dla których rysujemy wykres (potrzebny do plot)
    :param tab: tablica współczynników
    :return:
    """
    j = len(tab)
    y = 0
    for i in range(j):
        y += tab[i] * x ** i
    return y


def poly_plot(tab, a, b, x1):
    """
    :param tab: tabela współczynników
    :param a: dolne ograniczenie przedziału
    :param b: górne ograniczenie przedziału
    :param x1: wartość x dla której znaleziono miejsce zerowe
    :return:
    """
    # zmienna x_range przechowuje przedział x'ów dla których rysujemy wykres
    x_range = np.arange(a, b + 1)
    plt.plot(x_range, poly_y_for_plot(x_range, tab))
    plt.plot(x1, horner.horner_result(tab, x1), 'ro')
    plt.show()


def plot(f, a, b, x1):
    """
        :param f: wzór funkcji
        :param a: dolne ograniczenie przedziału
        :param b: górne ograniczenie przedziału
        :param x1: wartość x dla której znaleziono miejsce zerowe
        :return:
        """
    # zmienna x_range przechowuje przedział x'ów dla których rysujemy wykres
    x_range = np.arange(a, b + 1)
    plt.plot(x_range, f(x_range))
    plt.plot(x1, f(x1), 'ro')
    plt.show()
# def trig_plot()
