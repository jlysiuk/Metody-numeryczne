import numpy as np
import bisections
import plotting
import regula_falsi


def choose_fuction_type():
    print('Chcesz znaleźć miejsce zerowe funkcji:\n'
          '1 - Wielomianowej\n'
          '2 - Trygonometrycznej\n'
          '3 - Wykładniczej\n'
          '4 - Złożonej')

    case = int(input('Wybierz numer od 1 do 4: '))

    if case == 1:
        print('Wybrano funkcję wielomianową')
        tab = input('Wielomian przyjmie postać: W(x) = tab[0] + tab[1]*x + tab[2]*x*x + ...\n'
                    'Podaj tablicę współczynników : ')
        tab = tab.split()
        i = len(tab)

        for i in range(i):
            tab[i] = float(tab[i])
        print(tab)
        print('Chcesz zatrzymać poszukiwanie za pomocą:\n'
              '1 - Ustawienia tolerancji (epsilon)\n'
              '2 - Ustawienia limitu operacji')
        case = int(input('Wybierz 1 lub 2: '))
        if case == 1:
            a = float(input('Wybierz początek przedziału: '))
            b = float(input('Wybierz koniec przedziału: '))
            d = float(input('Wybierz tolerancję: '))
            plotting.poly_plot(tab, a, b, bisections.bisection_tolerance_poly(tab, a, b, d)[0])
            plotting.poly_plot(tab, a, b, regula_falsi.falsi_tolerance_poly(tab, a, b, d)[0])
            print('Miejsce zerowe wyznaczone metodą bisekcji to:', bisections.bisection_tolerance_poly(tab, a, b, d))
            print('Miejsce zerowe wyznaczone metodą regula falsi to:', regula_falsi.falsi_tolerance_poly(tab, a, b, d))
        if case == 2:
            a = float(input('Wybierz początek przedziału: '))
            b = float(input('Wybierz koniec przedziału: '))
            i = int(input('Wprowadź limit iteracji: '))
            plotting.poly_plot(tab, a, b, bisections.bisection_iteration_poly(tab, a, b, i))
            plotting.poly_plot(tab, a, b, regula_falsi.falsi_iteration_poly(tab, a, b, i))
            print('Miejsce zerowe wyznaczone metodą bisekcji to:', bisections.bisection_iteration_poly(tab, a, b, i))
            print('Miejsce zerowe wyznaczone metodą regula falsi to:', regula_falsi.falsi_iteration_poly(tab, a, b, i))

    elif case == 2:
        print('Wybrano funkcję trygonometryczną')
        case = int(input('1 - Sinus\n'
                         '2 - Cosinus\n'
                         'Wybierz funkcję sin lub cos: '))
        if case == 1:
            print('Funkcja przyjmnie postać sin(x)')
            f = lambda x: np.sin(x)
        if case == 2:
            print('Funkcja przyjmnie postać cos(x)')
            f = lambda x: np.cos(x)
        choose_method(f)

    elif case == 3:
        print('Wybrano funkcję wykładniczą')
        a = float(input('Funkcja przybierze postać a * b^x + c. Podaj a:'))
        b = float(input('Podaj b:'))
        c = float(input('Podaj c:'))
        f = lambda x: a * (b ** x) + c
        print(f'Twoja funkcja to ({a}) + ({b})^x + ({c})')
        choose_method(f)

    elif case == 4:
        print('Wybrano funkcję złożoną.\n'
              'Dostępne funkcje:\n'
              '1 - f(x) = 2.5 * x^(sin(x)) - 17\n'
              '2 - f(x) = cos(2^x)\n'
              '3 - f(x) = x^(3x^2 + 1.5x - 12) - 2')
        case = int(input("Wybierz od 1, 2 lub 3: "))
        if case == 1:
            f = lambda x: 2.5 * x ** (np.sin(x)) - 17
        if case == 1:
            f = lambda x: np.cos(2 ** x)
        if case == 1:
            f = lambda x: x ** (3 * x ** 2 + 1.5 * x - 12) - 2
        choose_method(f)


def choose_method(f):
    """
    :param f: funkcja której miejsce zerowe chcemy określić
    :return:
    """
    print('Chcesz zatrzymać poszukiwanie za pomocą:\n'
          '1 - Ustalenia tolerancji (epsilon)\n'
          '2 - Ustalenia limitu operacji')
    case = int(input('wybierz 1 lub 2: '))
    a = float(input('Wybierz początek przedziału: '))
    b = float(input('Wybierz koniec przedziału: '))
    if case == 1:
        d = float(input('Wybierz tolerancję: '))
        print('Miejsce zerowe wyznaczone metodą bisekcji to:', bisections.bisection_tolerance(f, a, b, d))
        print('Miejsce zerowe wyznaczone metodą regula falsi to:', regula_falsi.falsi_tolerance(f, a, b, d))
    if case == 2:
        i = int(input('Wprowadź limit iteracji: '))
        print('Miejsce zerowe wyznaczone metodą bisekcji to:', bisections.bisection_iteration(f, a, b, i))
        print('Miejsce zerowe wyznaczone metodą regula falsi to:', regula_falsi.falsi_iteration(f, a, b, i))
