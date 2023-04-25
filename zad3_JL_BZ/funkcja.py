import numpy as np  # do obliczeń trygonometrycznych oraz generowania argumentów funkcji do stworzenia wykresu
import sympy as sp  # do tworzenia wzorów funkcji z parametrem oraz obliczeń pochodnych
from horner import horner


def wartosc_funkcji(arg_x, wybor):
    """Zwracanie wartości wybranej funkcji dla argumentu x

            Parametry
            ----------
            arg_x : float
                wartosc argumentu x
            wybor  : String
                wybór funkcji A, B, C, D lub E
            Dane wyjsciowe
            -------
            wart_fun : float
                wartość funkcji dla argumentu x
    """
    if wybor == "A":    # A dla funkcji wielomianowej
        wart_fun = horner([5, 2, -1, 5], arg_x)  # obliczenie wartosci schematem hornera
    elif wybor == "B":  # B dla funkcji trygonometrycznej
        wart_fun = 5 * np.cos(arg_x) - 3 * np.sin(arg_x)
    elif wybor == "C":  # C dla modułu
        wart_fun = abs(arg_x - 5)
    elif wybor == "D":  # D dla liniowej
        wart_fun = arg_x - 5
    elif wybor == "E":  # D dla liniowej
        wart_fun = abs(np.cos(arg_x) - 0.5)
    else:
        print("Podano nieprawidlowa wartosc. Wybierz a, b, c lub d")
        wart_fun = None
    return wart_fun     # zwróc wartość funkcji dla konkretnego argumentu x


def wzor_funkcji(wybor):
    """Zwracanie wzoru funkcji z parametrem x

            Parametry
            ----------
            wybor  : String
                wybór funkcji A, B, C, D lub E
            Dane wyjsciowe
            -------
            wzor_fun : Symbol
                wzór funkcji zapisany ze zmienną x
    """
    arg_x = sp.Symbol('x')
    if wybor == "A":  # A dla funkcji wielomianowej
        wzor_fun = horner([5, 2, -1, 5], arg_x)  # obliczenie wartosci schematem hornera
    elif wybor == "B":  # B dla funkcji trygonometrycznej
        wzor_fun = 5 * sp.cos(arg_x) - 3 * sp.sin(arg_x)
    elif wybor == "C":  # C dla modułu
        wzor_fun = abs(arg_x - 5)
    elif wybor == "D":  # D dla liniowej
        wzor_fun = arg_x - 5
    elif wybor == "E":  # D dla liniowej
        wzor_fun = abs(sp.cos(arg_x) - 0.5)
    else:
        print("Podano nieprawidlowa wartosc. Wybierz a, b, c lub d")
        wzor_fun = None
    return wzor_fun     # zwroc wzór funkcji
