import numpy as np
from matplotlib import pyplot as plt

import front
import horner
import plotting
import regula_falsi





#
# print(bisections.bisection_tolerance_poly([12, 3, 2, 0, -5], 0.1, 3.2, 0.001))
# print(bisections.bisection_iteration_poly([12, 3, 2, 0, -5], 0.1, 3.2, 100))
# print(regula_falsi.falsi_tolerance(f, 0.1, 3.2, 0.001))
# print(regula_falsi.falsi_iteration(f, 0.1, 3.2, 66))
# print(regula_falsi.falsi_iteration_poly([12, 3, 2, 0, -5], 0.1, 3.2, 66))
# print(regula_falsi.falsi_tolerance(f, 0.1, 3.2, 0.001))
# print(regula_falsi.falsi_tolerance_poly([12, 3, 2, 0, -5], 0.1, 3.2, 0.001))
# print(g(2.0))
# print(horner.horner_result([-2, 3, 2, -7.5], 2.0))

front.choose_fuction_type()
# a = -5
# b = 1
# tab = [-7, 2, 1]
# x_range = np.arange(a, b)
# plt.plot(x_range, plotting.poly_y_for_plot(x_range, tab))
# plt.plot(-3.0, horner.horner_result(tab, -3.0), 'ro')
# plt.show()
# front.choose_fuction_type()



# i = len(tab)
# y = 0
# a = 0
# x = np.arange(-3, 2)
# while i > 0:
#     i = i - 1
#     a = a + 1
#     y[i] = tab[i]
# plt.title("Matplotlib demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x, y)
# plt.show()
#
# print(y)
# tab = [-7, 2, 1]





# tab = input('Wielomian przyjmie postać: W(x) = tab[0] + tab[1]*x + tab[2]*x*x + ...\n'
#                     'Podaj tablicę współczynników : ')
# tab = tab.split()
# i = len(tab)
#
# for i in range(i):
#     tab[i] = float(tab[i])
# x = np.arange(-4, 4)
# plt.plot(x, plotting.poly_y_for_plot(x, tab))
#
# plt.show()





