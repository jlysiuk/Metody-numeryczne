from typing import Callable, Any

import numpy as np
import bisections


def choose_fuction_type():
    print('chcesz znaleźć miesjce zerowe funkcji:\n'
          '1 - wielomianowej\n'
          '2 - trygonometrycznej\n'
          '3 - wykładniczej\n'
          '4 - złożonej')

    case = int(input('wybierz numer od 1 do 4: '))

    if case == 1:
        print('Wybrano funkcję wielomianową')
        tab = input('Wielomian przyjmie postać: W(x) = tab[0] + tab[1]*x + tab[2]*x*x + ...\n'
                    'podaj tablicę współczynników : ')
        tab = tab.split()
        i = len(tab)

        for i in range(i):
            tab[i] = float(tab[i])

        print('chcesz znaleźć miesjce zerowe funkcji za pomocą:\n'
              '1 - metody bisekcji\n'
              '2 - reguły falsi')
        case = int(input('wybierz 1 lub 2: '))
        if case == 1:
            print('wybrano metodę bisekcji. Chcesz zatrzymać poszukiwanie za pomocą:\n'
                  '1 - ustawienia tolerancji (epsilon)\n'
                  '2 - ustawienia limitu iteracji')
            case = int(input('wybierz 1 lub 2: '))
            if case == 1:
                a = float(input('wybierz początek przedziału: '))
                b = float(input('wybierz koniec przedziału: '))
                d = float(input('wybierz tolerancję: '))
                print('miejsce zerowe to:', bisections.bisection_tolerance_poly(tab, a, b, d))
            # if case == 2:
            # zrob do iteracyjnego
        if case == 2:
            print('wybrano regułę falsi.')
            # dopisz do falsi

    elif case == 2:
        print('Wybrano funkcję trygonometryczną')
        case = int(input('1 - sinus\n'
                         '2 - cosinus\n'
                         'Wybierz funkcję sin lub cos: '))
        if case == 1:
            print('Funkcja przyjmnie postać sin(x)')
            f = lambda x: np.sin(x)
        if case == 2:
            print('Funkcja przyjmnie postać cos(x)')
            f = lambda x: np.cos(x)
        print('chcesz znaleźć miesjce zerowe funkcji za pomocą:\n'
              '1 - metody bisekcji\n'
              '2 - reguły falsi')
        case = int(input('wybierz 1 lub 2: '))
        if case == 1:
            print('wybrano metodę bisekcji. Chcesz zatrzymać poszukiwanie za pomocą:\n'
                  '1 - ustawienia tolerancji (epsilon)\n'
                  '2 - ustawienia limitu operacji')
            case = int(input('wybierz 1 lub 2: '))
            if case == 1:
                a = float(input('wybierz początek przedziału: '))
                b = float(input('wybierz koniec przedziału: '))
                d = float(input('wybierz tolerancję: '))
                print('miejsce zerowe to:', bisections.bisection_tolerance(f, a, b, d))
            # if case == 2:
            # zrob do iteracyjnego
        if case == 2:
            print('wybrano regułę falsi.')
            # dopisz do falsi
    elif case == 3:
        print('Wybrano funkcję wykładniczą')
    elif case == 4:
        print('Wybrano funkcję złożoną')
